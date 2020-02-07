import collections
class Node:
  def __init__(self, val = 0, neighbors = []):
    self.val = val
    self.neighbors = neighbors

  def dfsPrint(self,start):
    stack = []
    seen = set()
    stack.append(start)

    while stack: 
      curr = stack.pop()

      if (curr not in seen): 
        seen.add(curr)
        print(curr.val)
      
      for neighbor in curr.neighbors:
        if (neighbor not in seen):
          stack.append(neighbor)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.neighbors = [e,d,c,b]
b.neighbors = [g,c,a]
c.neighbors = [d,b,a]
d.neighbors = [h,e,c,a]
e.neighbors = [a,d,f]
f.neighbors = [h,g]
g.neighbors = [f,b]
h.neighbors = [d,f]

a.dfsPrint(a)