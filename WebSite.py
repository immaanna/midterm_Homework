from TdP_collections.tree.tree import Tree
from TdP_collections.hash_table.sorted_table_map import SortedTableMap
import Element as elem


def WebSite(Tree, SortedTableMap):
    class _Node:
        __slots__ = '_url', '_parent', '_children'

        def __init__(self, url, parent=None):
            self._url = url
            self._parent = parent
            self._children = SortedTableMap()  # sorted table map

        # ----- Nested Class -----#

    class Position(Tree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._url

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    # ----- costruttore WebSite ---
    def __init__(self, host):
        self._root = host
        self._size = 1

    def Tree(self, elem):
        url = elem._url.split("/")
        parent=self._root
        for i in range(1, len(url)):
            parent=_create_node(url[i],i,parent)

    def _create_node(self, url,i):

        if i==1:
            p = self._make_position(self._Node(url, self._root))
            self._root._children.__setitem__(self, url,p)
            self._add_child(p, self._root)
            self._size += 1
            return p
        else:

            self._root._children.__setitem__(self, url,1)
            p = self._make_position(self._Node(url, self._root._children))
            self._add_child(p, self._root)
            self._size += 1
            return





    def _add_child(self, p, parent):
        node = self._validate(p)
        parent._children.append(node)

    def __isDir(self, elem):
        pass

    def __isPage(self, elem):
        pass

    def __hasDir(self, ndir, cdir):
        pass

    def __newDir(self, ndir, cdir):
        pass

    def __hasPage(self, npag, cdir):
        pass

    def __newPage(self, npag, cdir):
        pass

    def getHomePage(self):
        pass

    def getSiteString(self):
        pass

    def insertPage(self, url, content):
        pass

    def getSiteFromPage(self, page):
        pass
