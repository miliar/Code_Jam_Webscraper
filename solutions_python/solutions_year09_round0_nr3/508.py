target="welcome to code jam"

source = open('C-small-attempt0.in','rb')

cases = int(source.readline())

class Node:
    maxcnt = 0
    def __init__(self, idx, level):
        self.idx = idx
        self.children = list()
        self.level = level
    def put(self, idxs):
        if len(self.children):
            for x in self.children:
                x.put(idxs)
        else:
            for idx in idxs:
                if idx > self.idx:
                    if self.level == len(target)-1:
                        Node.maxcnt = Node.maxcnt +1
                    else:
                        self.children.append(Node(idx,self.level+1))
                    



for x in xrange(cases):
    idx = 0
    rootnode = Node(-1, 0)
    Node.maxcnt = 0
    data = source.readline()
    if len(target)>len(data):
        print "Case #%s: %04d" % (x+1, Node.maxcnt)
        continue
    while idx < len(target):
        z = data.find(target[idx])
        idxs = list()
        while z != -1:
            idxs.append(z)
            z = data.find(target[idx],z+1)
        rootnode.put(idxs)
        idx = idx + 1
    print "Case #%s: %04d" % (x+1, Node.maxcnt % 1000)