import sys

class Tree:
    def __init__(self, s):
        aa = s.split(' ')
        a = [x.strip() for x in aa if len(x.strip()) > 0]
        a = a[1:-1]
        #print a
        self.w = float(a[0])
        if len(a) > 1:
            self.feature = a[1]
        else:
            self.feature = ""
        self.sub = []
        s = ""
        dep = 0
        for c in a[2:]:
            s += c + " "
            if c == '(':
                dep += 1
            elif c == ')':
                dep -= 1
            if dep == 0:
                #print "sub:",s
                self.sub.append(Tree(s))
                s = ""
        #print self.w, len(self.sub)

    def check(self, fs, p):
        p *= self.w
        if self.sub:
            if self.feature in fs:
                p = self.sub[0].check(fs, p)
            else:
                p = self.sub[1].check(fs, p)
        return p
lines = sys.stdin.readlines()
#lines = """1
#13
#(0.2 furry
#  (0.81 fast
#    (0.3)
#    (0.2)
#  )
#  (0.1 fishy
#    (0.3 freshwater
#      (0.01)
#      (0.01)
#    )
#    (0.1)
#  )
#)
#1
#beaver 2 furry freshwater""".split("\n")
lines = [l.strip() for l in lines]
N = int(lines[0])
lno = 1
for cn in range(1, N + 1):
    print "Case #%d:" % cn
    dcount = int(lines[lno])
    lno += 1
    dtree = ""
    for i in range(dcount):
        dtree += " " + lines[lno]
        lno += 1
    dtree = dtree.replace('(', ' ( ')
    dtree = dtree.replace(')', ' ) ')
    #print dtree
    t = Tree(dtree)
    ans = int(lines[lno])
    lno += 1
    for i in range(ans):
        features = lines[lno].split(' ')[2:]
        lno += 1
        print "%.7f" % t.check(features, 1.0)
    
