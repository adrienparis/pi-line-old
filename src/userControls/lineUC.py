import maya.cmds as cmds
from pymel.all import *

from .UC import *

class LineUC(UserControl):
    increment = 0
    selectedColor = hexToRGB(0x5285a6)

    def __init__(self, parent, text, info="", icon=None):
        UserControl.__init__(self, parent)
        self.icon = icon
        self.text = text
        self.info = info
        self.selected = False
        self.name = self.text + "Line" + self.name + str(LineUC.increment)
        LineUC.increment += 1

    def load(self):
        self.layout = cmds.formLayout(self.name, parent=self.parentLay, h=17, bgc=self.selectedColor, ebg=self.selected)
        self.gmc = cmds.popupMenu("gmc",parent=self.layout, button=1, pmc=Callback(self.clickCommand))
        self.gmcs = cmds.popupMenu("gmcs", parent=self.layout, button=1, sh=True, pmc=Callback(self.clickCommandShift))
        self.nameTextLay = cmds.text(parent=self.layout, label=self.text, al="left")
        self.infoTextLay = cmds.text(parent=self.layout, label=self.info, al="right")

        af = []
        an = []
        ac = []

        if self.icon is None:
            af.append((self.nameTextLay, "left", 2))
        else:
            self.iconLay = cmds.image(parent=self.layout, image=getIcon(self.icon))
            ac.append((self.nameTextLay, "left", 2, self.iconLay))
            af.append((self.iconLay, "top", 1))
            af.append((self.iconLay, "bottom", 1))
            af.append((self.iconLay, "left", 1))
            an.append((self.iconLay, "right"))

        af.append((self.nameTextLay, "top", 2))
        af.append((self.nameTextLay, "bottom", 2))
        an.append((self.nameTextLay, "right"))


        af.append((self.infoTextLay, "top", 1))
        af.append((self.infoTextLay, "bottom", 1))
        ac.append((self.infoTextLay, "left", 1, self.nameTextLay))
        af.append((self.infoTextLay, "right", 5))

        # if self.icon is None:
        #     af += [(self.nameTextLay, "top", 2), (self.nameTextLay, "bottom", 2), (self.nameTextLay, "left", 2), (self.nameTextLay, "right", 2)]
        #     cmds.formLayout(self.layout, edit=True,
        #                 attachForm=[(self.nameTextLay, "top", 2), (self.nameTextLay, "bottom", 2), (self.nameTextLay, "left", 2), (self.nameTextLay, "right", 2)])
        # else:
        #     self.iconLay = cmds.image(parent=self.layout, image=getIcon(self.icon))
        #     cmds.formLayout(self.layout, edit=True,
        #                     attachForm=[(self.nameTextLay, "top", 2), (self.nameTextLay, "bottom", 2), (self.nameTextLay, "right", 2), 
        #                                 (self.iconLay, "top", 1), (self.iconLay, "left", 0), (self.iconLay, "bottom", 1)],
        #                     attachControl=[(self.nameTextLay, "left", 2, self.iconLay)],
        #                     attachNone=[(self.iconLay, "right")])
        cmds.formLayout(self.layout, edit=True,
                        attachForm=af,
                        attachControl=ac,
                        attachNone=an)
    def refresh(self):
        cmds.text(self.nameTextLay, e=True, label=self.text)
        cmds.text(self.infoTextLay, e=True, label=self.info)
        cmds.image(self.iconLay, e=True, image=getIcon(self.icon))

    def setIcon(self, icon):
        self.icon = icon

    def selection(self, b):
        self.selected = b
        cmds.formLayout(self.layout, e=True, ebg=self.selected)

    def clickCommand(self):
        self.mods = 0
        self.runEvent("click", self, self.mods)
        # cmds.popupMenu("gmc", q=True, exists=True)

    def clickCommandShift(self):
        self.mods = 1
        self.runEvent("click", self, self.mods)
        # self.gmcs = cmds.popupMenu("gmcs", parent=self.layout, button=1, sh=True, pmc=Callback(self.clickCommandShift))