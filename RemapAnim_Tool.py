import maya.cmds as cmds

def remapAnimationCurves():
    """Remaps the animation curves from one object to another, based on the remapping options selected in the UI."""

    # Get the remapping options selected in the UI.
    remapX = cmds.optionMenu("remapXOptionMenu", q=True, value=True)
    remapY = cmds.optionMenu("remapYOptionMenu", q=True, value=True)
    remapZ = cmds.optionMenu("remapZOptionMenu", q=True, value=True)

    # Get the two selected objects.
    objects = cmds.ls(sl=True)

    # Iterate over the objects and remap the animation curves.
    for object in objects:
        # Get the animation curves for the object.
        animationCurves = cmds.listConnections(object, type="animCurve")

        # Iterate over the animation curves and remap them.
        for animationCurve in animationCurves:
            # Get the attribute that the animation curve is connected to.
            attribute = cmds.listConnections(animationCurve, type="attribute")[0]

            # Get the remapped attribute name.
            remappedAttributeName = ""
            if attribute == "translateX":
                remappedAttributeName = "translateY"
            elif attribute == "translateY":
                remappedAttributeName = "translateZ"
            elif attribute == "translateZ":
                remappedAttributeName = "translateX"
            elif attribute == "rotateX":
                remappedAttributeName = remapX
            elif attribute == "rotateY":
                remappedAttributeName = remapY
            elif attribute == "rotateZ":
                remappedAttributeName = remapZ

            # Connect the remapped animation curve to the remapped attribute.
            cmds.connectAttr(animationCurve, object + "." + remappedAttributeName)

# Create the UI.
window = cmds.window(title="Remap Animation Curves")
cmds.columnLayout()

# Add the X remapping option menu.
cmds.optionMenu("remapXOptionMenu", label="Remap X", changeCommand=remapAnimationCurves)
cmds.menuItem(label="X")
cmds.menuItem(label="-X")
cmds.menuItem(label="Y")
cmds.menuItem(label="-Y")
cmds.menuItem(label="Z")
cmds.menuItem(label="-Z")

# Add the Y remapping option menu.
cmds.optionMenu("remapYOptionMenu", label="Remap Y", changeCommand=remapAnimationCurves)
cmds.menuItem(label="X")
cmds.menuItem(label="-X")
cmds.menuItem(label="Y")
cmds.menuItem(label="-Y")
cmds.menuItem(label="Z")
cmds.menuItem(label="-Z")

# Add the Z remapping option menu.
cmds.optionMenu("remapZOptionMenu", label="Remap Z", changeCommand=remapAnimationCurves)
cmds.menuItem(label="X")
cmds.menuItem(label="-X")
cmds.menuItem(label="Y")
cmds.menuItem(label="-Y")
cmds.menuItem(label="Z")
cmds.menuItem(label="-Z")

# Add the Remap button.
cmds.button(label="Remap", command=lambda: remapAnimationCurves())

cmds.showWindow(window)
