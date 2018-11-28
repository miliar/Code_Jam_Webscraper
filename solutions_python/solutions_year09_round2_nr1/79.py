from pyparsing import *

feature = Word(alphas)
def make_float(f):
    return float(f[0])

class Node(object):
    def __init__(self, w, feature, l, r):
        self.weight = w
        self.feature = feature
        self.left = l
        self.right = r
    def __repr__(self):
        if self.feature is not None:
            return "w: %.2f f: %s l: (\n\t%s)\nr: (\n\t%s)" % (self.weight, self.feature, self.left, self.right)
        else:
            return "w: %.2f" % self.weight

def parse_tree(l):
    if len(l) == 1:
        return Node(l[0], None, None, None)
    elif len(l) == 4:
        return Node(l[0], l[1], l[2], l[3])
    else:
        raise ValueError, "%d elements." % len(l)

tree = Forward()
tree << Literal('(').suppress() + (Word("0123456789-.").setParseAction(make_float)
         + Optional(feature + tree + tree)) + Literal(')').suppress()
tree.setParseAction(parse_tree)

class DTree(object):
    def __init__(self, s):
        self.arr = tree.parseString(s)[0]
    def eval(self, features, root=None, p=1.0):
        if root is None:
            root = self.arr
        next_p = p * root.weight
        if root.feature is not None:
            if root.feature in features:
                branch = root.left
            else:
                branch = root.right
            return self.eval(features, branch, next_p)
        else:
            return next_p

def parse_input(fname):
    infile = open(fname)
    ncases = int(infile.readline())
    cases = []
    for i in range(ncases):
        ntreelines = int(infile.readline())
        treearr = []
        for j in range(ntreelines):
            treearr.append(infile.readline())
        tree = '\n'.join(treearr)
        nanimallines = int(infile.readline())
        animals = []
        for j in range(nanimallines):
            animals.append(set(infile.readline().split()[2:]))
        cases.append((tree, animals))
    infile.close()
    return cases

if __name__ == '__main__':
    s = """
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
""".strip()
    import glob
#    fname = glob.glob("A-small*.in")[0]
    fname = glob.glob("A-large*.in")[0]
    cases = parse_input(fname)
    for ndx,(tr,animals) in enumerate(cases):
        t = DTree(tr)
        print "Case #%d: " % (ndx+1)
        for a in animals:
            p = t.eval(a)
            print "%.7f" % p
