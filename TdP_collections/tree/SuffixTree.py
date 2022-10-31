from TdP_collections.tree.tree import Tree

class SuffixTree(Tree):

  #----- Nested Class -----#
  class _Node:
    __slots__ = '_start', '_end', '_parent', '_children'
    
    def __init__(self, n, start, end, parent=None):
      self._start = start
      self._end = end
      self._parent = parent
      self._children = []

  #----- Nested Class -----#
  class Position(Tree.Position):
    
    def __init__(self, container, node):
      self._container = container
      self._node = node
    
    def element(self):
      return self._node._n, self._node._start, self._node._end

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

  #---Main Methods----#
  def __init__(self):
    self._root = None
    self._size = 0
    self.D = []

  def SuffixTree(self,S):
    self._root = self._Node(0, 0, 0)
    self._size=1
    for i in range(0,len(S)):
      self.D.append(S[i])
      for x in range(0,len(S[i])):
        self._find_node(x,len(S[i]),i+1,S)

  def _match(self,stringa,stringap):
    length=min(len(stringa),len(stringap))
    for i in range (1,length):
      if stringa[i]!=stringap[i]:
        return i
    return length-1

  def _find_node(self, start, end, n, S):
    if len(self._root._children) == 0:
      p = self._make_position(self._Node(n, start, end, self._root))
      self._add_child(p, self._root)
      self._size += 1
      return
    else:
      for c in self._root._children:
        stringa = S[n - 1][start:end] + '$'
        stringan = S[c._n - 1][c._start:c._end] + '$'
        if stringa[0] != stringan[0]:
          continue
        else:
          pos = self._make_position(c)
          self.__add_to_child(pos,start,end,n,S)
          return

      p = self._make_position(self._Node(n, start, end, self._root))
      self._add_child(p, self._root)
      self._size += 1

  def __add_to_child(self, p, start, end, n, S):
    node = self._validate(p)
    tupla = p.element()
    np = tupla[0]
    sn = tupla[1]
    en = tupla[2]
    strnode = S[np-1][sn:en] + '$'
    stringa = S[n - 1][start:end] + '$'
    match = self._match(stringa, strnode)
    if len(node._children) == 0:
      if stringa == strnode:
        if n not in node._marker:
            node._marker.append(n)
            return
      else:
        if sn == 0:
          node._end = match 
        else:
          node._end = match+sn
        start_2 = start+ match
        p1 = self._make_position(self._Node(n, start_2, end, node))
        p2 = self._make_position(self._Node(np, node._end, en, node))
        self._add_child(p1, node)
        self._add_child(p2, node)
        self._size += 2
        return
    else:
      if len(strnode)-1 > match:
        children = node._children
        self._remove_child(p)
        node._end = match+sn
        start_2 = start+ match
        p1 = self._make_position(self._Node(n, start_2, end, node))
        p2 = self._make_position(self._Node(np, node._end, en, node))
        self._add_child(p1, node)
        self._add_child(p2, node)
        nf = self._validate(p2)
        self._size += 2
        for c in children:
          self._add_child(self._make_position(c),nf)
          c._parent = nf
      else:  
        for c in node._children:
          strch = S[c._n - 1][c._start:c._end] + '$'
          stringa = S[n - 1][start+match:end] + '$'
          if stringa == strch:
            if n not in c._marker:
              c._marker.append(n)
              return
          elif stringa[0] == strch[0]:
            if n not in node._marker:
              node._marker.append(n)
            self.__add_to_child(self._make_position(c), start+match,end,n,S)
            return 
        p1 = self._make_position(self._Node(n, start+match, end, node))
        self._add_child(p1, node)
        self._size += 1
        return        
#--------------------ADT TREE--------------------------#
  def getNodeLabel(self,P):
    node = self._validate(P)
    word = self.D[node._n -1]
    return word[node._start:node._end]

  def pathString(self,P):
    node = self._validate(P)
    if node._n == 0:
     return
    if node._parent._n == 0:
      return self.getNodeLabel(P)
    else:
      return self.pathString(self._make_position(node._parent))+self.getNodeLabel(P) 

  def getNodeDepth(self,P):
    node = self._validate(P)
    if node == self._root:
      return 0
    return len(self.pathString(P))

  def getNodeMark(self,P):
    node = self._validate(P)
    return node._marker

  def child(self,P,s):
    node = self._validate(P)
    if len(node._children) == 0:
      return None
    for c in node._children:
      label = self.getNodeLabel(self._make_position(c))
      if len(label) == 0:
        continue
      elif label[0] !=s [0]:
        continue
      else:
        if len(s) == 1:
          return self._make_position(c)
        if len(label) >= len(s):
          for i in range(1,len(s)):
            if label[i] != s[i]:
              return None
          return self._make_position(c)
        elif len(label) < len(s):
          for i in range(1,len(label)):
            if label[i] != s[i]:
              return None
          if len(c._children) > 0:
            for cc in c._children:
              l1 = self.getNodeLabel(self._make_position(cc))
              if len(l1) == 0:
                return self._make_position(c)
              else:
                if l1[0] == s[len(label)]:
                  return self.child(self._make_position(c), s[len(label):len(s)])
                else:
                  return self._make_position(c)
          else:
            return self._make_position(c)
  #-----------------------------------------#

  def root(self):
    return self._make_position(self._root)
  
  def _add_child(self, p, parent):
    node = self._validate(p)
    parent._children.append(node)
    if node._n not in parent._marker and parent != self._root:
      parent._marker.append(node._n)

  def _remove_child(self,p):
    node = self._validate(p)
    node._children = []

  def __len__(self):
    return self._size

  def children(self, p):
    node = self._validate(p)
    for child in node._children:
      c = self._make_position(child)
      yield c

  def parent(self, p):
    node = self._validate(p)
    return self._make_position(node._parent)

  def is_empty(self):
    return self._size == 0

  def _printTree(self):
        for p in self.positions():
            tupla = p.element()
            # node = self._validate(p)
            # print("Path")
            print(self.pathString(p))
            print("Label" + " " + self.getNodeLabel(p))
            #if tupla[0] != 0:
                #print("Path" + " " + self.pathString(p))
            # if tupla[0] != 0:
            #    print("Padre" + " " + self.getNodeLabel(self._make_position(node._parent)))
            #print("Tupla elemento")
            print(tupla)

            # if tupla[0]==0 and tupla[1]==0 and tupla[2]==0:
            #    c=self.child(p,"alivec")
            # if(p==None):
            #    print("None")
            #   return

            #    print(self.getNodeLabel(c))

