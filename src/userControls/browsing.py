class Browsing(object):
    class item():
        def __init__(self, name, elem, image=None, info="", icon=None):
            self.name = name
            self.elem = elem
            self.image = image
            self.icon = icon
            self.info = info
            self.deep = 0
            self.parent = None
            self.displayElem = None
            self.selected = False
            
        def setParent(self, parent):
            if self.parent is not None:
                self.parent.removeChildren(self)
            parent.addChildren(self)

    class folder(item):
        def __init__(self, name, elem):
            Browsing.item.__init__(self, name, elem)
            self.childrens = []
            self.icon = "arrowBottom"
            self.isDeployed = True
            self.area = None

        def deploying(self, val):
            self.isDeployed = val
            if val:
                self.icon = "arrowBottom"
            else:
                self.icon = "arrowRight"
            self.displayElem.icon = self.icon
            self.displayElem.refresh()
            self.area.visibility(self.isDeployed)
            # cmds.formLayout(self.area, e=True, vis=self.isDeployed)

        def deployingAll(self, val):
            self.deploying(val)
            for f in self.childrens:
                if f.__class__ is Browsing.folder:
                    Browsing.folder.deployingAll(f, val)

        def addChildren(self, child):
            self.childrens.append(child)
            child.parent = self

        def removeChildren(self, child):
            self.childrens.remove(child)
            child.parent = None
        
        def getAllParent(self):
            if self.parent is None:
                return "/"
            return self.getAllParent() + "/" + self.name

    def __init__(self):
        # super(Browsing, self).__init__()
        self.folders = {}
        self.items = {}
        self.root = Browsing.folder(".", None)
        self.selecteds = []
        self.multiSelect = True
        self.addable = True
    
    def deleteAllItemsFolders(self):
        self.folders = {}
        self.items = {}
        self.root = Browsing.folder(".", None)

    def addFolder(self, name, elem, parent=None):
        f = Browsing.folder(name, elem)

        if parent is None:
            f.setParent(self.root)
            f.deep = 1
        else:
            f.setParent(parent)
            f.deep = f.parent.deep + 1
        self.folders[elem] = f
        return f
    
    def addItem(self, name, elem, parent=None, image=None, info="", icon=None):
        i = Browsing.item(name, elem, image=image, info=info, icon=icon)

        if parent is None:
            i.setParent(self.root)
        else:
            i.setParent(parent)
            i.deep = i.parent.deep + 1
        self.items[elem] = i
        return i

    def importBrows(self, imp):
        self.root = imp.root

    def select(self, selection, value):
        '''display the lines in selection as selected in the tree
        selection: the lines to be select
        value: True to select
        '''
        pass
