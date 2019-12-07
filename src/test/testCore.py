import os
import sys
from imp import reload
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "")
sys.path.append(path)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import plUser as user
import core

import userControls as UC


def mainUI():
    
    win = UC.WindowUC(u"Pi-Line")
    win.load()

    cpBrd = UC.CupboardUC(win)
    cpBrd.create()
    cpBrd.attach(top=UC.Attach.FORM, bottom=UC.Attach.FORM, left=UC.Attach.FORM, right=UC.Attach.FORM, margin=0)

    win.applyAttach()


print(u"=====Start pi-Line=====")
# print("Merci pilou <3")
mainUI()
