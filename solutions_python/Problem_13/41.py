class Tree(object):
    def __init__(self, value, changeable = False):
        self.v = value
        self.c = changeable
        self.children = []
    def addChild(self, child):
        self.children.append(child)
    def value (self):
        if len(children):
            if value:
                return self.children[0].value() and self.children[1].value()
            else:
                return self.children[0].value() or self.children[1].value()
        else:
            return self.value
    def minChangesToGet(self, value):
        if len(self.children) == 0:
            if value == self.v:
                return 0
            else:
                return "IMPOSSIBLE"
        else:
            v1 = self.children[0].minChangesToGet(value)
            v2 = self.children[1].minChangesToGet(value)
            if v1 == "IMPOSSIBLE" and v2 == "IMPOSSIBLE":
                return "IMPOSSIBLE"
            elif v1 == "IMPOSSIBLE" or v2 == "IMPOSSIBLE":
                if v1 == "IMPOSSIBLE":
                    v = v2
                elif v2 == "IMPOSSIBLE":
                    v = v1
                if value != self.v:
                    return v
                else:
                    if self.c:
                        return v+1
                    else:
                        return "IMPOSSIBLE"
            else:
                v = min(v1,v2)
                if value != self.v:
                    return v
                elif not self.c:
                    return v1+v2
                else:
                    return min((v1 + v2), v+1)
    def dump(self):
        return "(%d %d %s)" % (self.v, self.c, ':'.join([c.dump() for c in self.children]))
f = file('A.txt')

N = int(f.readline())

for c in range(N):
    M, V = [int(x) for x in f.readline().strip().split()]
    G, C = [int(x) for x in f.readline().strip().split()]
    T = Tree(G, C)
    leaves = [T]
    newl = []
    for i in range(M-1):
        d = [int(x) for x in f.readline().strip().split()]
        if len(d) == 2:
            t = Tree(d[0],d[1])
        else:
            t = Tree(d[0])
        newl.append(t)
        leaves[0].addChild(t)
        if len(leaves[0].children) == 2:
            leaves.pop(0)
        if not leaves:
                leaves = newl
    print "Case #%d: %s" % (c+1, T.minChangesToGet(V))
        
