class Node:
      def __init__(self,changeable,val,child1=None,child2=None):
            self.changeable = changeable
            self.val = val
            self.child1 = child1
            self.child2 = child2
            self.get = None
            self.m = {}
      def getVal(self):
            if self.get: return self.get
            if self.val == "AND":
                  self.get = self.child1.getVal() and self.child2.getVal()
            elif self.val == "OR":
                  self.get = self.child1.getVal() or self.child2.getVal()
            else:
                  self.get = self.val
            return self.get
      def minChange(self,desiredVal):
            if desiredVal == self.getVal(): return 0
            if desiredVal in self.m: return self.m[desiredVal]
            mini = 10000
            if self.val == "AND":
                  if (desiredVal == 1):
                        if self.child1.minChange(1) != None and self.child2.minChange(1) != None:
                              mini = min(mini,self.child1.minChange(1)+self.child2.minChange(1))
                        if self.changeable:
                              if self.child1.minChange(1) != None and self.child2.minChange(1) != None:
                                    mini = min(mini,1+min(self.child1.minChange(1),self.child2.minChange(1)))
                              elif self.child1.minChange(1) != None:
                                    mini = min(mini,1+self.child1.minChange(1))
                              elif self.child2.minChange(1) != None:
                                    mini = min(mini,1+self.child2.minChange(1))
                              
                  else:
                        if self.child1.minChange(0) != None and self.child2.minChange(0) != None:
                              mini = min(mini,min(self.child1.minChange(0),self.child2.minChange(0)))
                        elif self.child1.minChange(0) != None:
                              mini = min(mini,self.child1.minChange(0))
                        elif self.child2.minChange(0) != None:
                              mini = min(mini,self.child2.minChange(0))
            elif self.val == "OR":
                  if (desiredVal == 1):
                        if self.child1.minChange(1) != None and self.child2.minChange(1) != None:
                              mini = min(mini,min(self.child1.minChange(1),self.child2.minChange(1)))
                        elif self.child1.minChange(1) != None:
                              mini = min(mini,self.child1.minChange(1))
                        elif self.child2.minChange(1) != None:
                              mini = min(mini,self.child2.minChange(1))
                  else:
                        if self.child1.minChange(0) != None and self.child2.minChange(0) != None:
                              mini = min(mini,self.child1.minChange(0)+self.child2.minChange(0))
                        if self.changeable:
                              if self.child1.minChange(0) != None and self.child2.minChange(0) != None:
                                    mini = min(mini,1+min(self.child1.minChange(0),self.child2.minChange(0)))
                              elif self.child1.minChange(0) != None:
                                    mini = min(mini,1+self.child1.minChange(0))
                              elif self.child2.minChange(0) != None:
                                    mini = min(mini,1+self.child2.minChange(0))
            else:
                  return None
            if mini==10000: return None
            self.m[desiredVal] = mini
            return mini


n = int(raw_input())
for i in xrange(n):
      m,v = [int(j) for j in raw_input().split()]
      nodes = []
      for j in xrange((m-1)/2):
            g,c = [int(q) for q in raw_input().split()]
            if g: nodes.append(Node(c,"AND"))
            else: nodes.append(Node(c,"OR"))
      for j in xrange((m-1)/2,m):
            nodes.append(Node(0,int(raw_input())))
      for j in xrange((m-1)/2):
            nodes[j].child1 = nodes[j*2+1]
            nodes[j].child2 = nodes[j*2+2]
      if nodes[0].minChange(v) == None:
            print "Case #%d: IMPOSSIBLE" % (i+1)
      else: print "Case #%d: %d" % (i+1,nodes[0].minChange(v))
