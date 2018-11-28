import sys
number = int(sys.stdin.readline().rstrip('\n'))
#print number

class Tree:
    def __init__(self, elem):
        self.tree = [elem, []]
    def __repr__(self):
        return self.tree.__repr__()
    def is_present(self, elem):
        if elem == self.tree[0]:
            return true
        if len(self.tree[1]) == 0:
            return false
        return self.tree[1].is_present(elem)
    def add_rec(self, dir, nbmkdir):
        #if dir[0] in [x.tree[0] for x in self.tree[1]]:
        for i in range(len(self.tree[1])):
            if self.tree[1][i].tree[0] == dir[0]:
                dir.pop(0)
                if len(dir) > 0:
                    nbmkdir = self.tree[1][i].add_rec(dir, nbmkdir)
                return nbmkdir
            else: 
                continue
        self.tree[1].append(Tree(dir[0]))
        nbmkdir += 1
        dir.pop(0)
        if len(dir) > 0:
            nbmkdir = self.tree[1][len(self.tree[1]) -1].add_rec(dir, nbmkdir)
        return nbmkdir

def power_off(t, k):
    for i in range(k, len(t)):
        t[k][1] = False


for i in range(number):
    l = sys.stdin.readline().rstrip('\n').split(' ')
    nexist = int(l[0])
    ncreate = int(l[1])
    exist = Tree('root')
    create = []
    #print nexist
    for n in range(nexist):
        line = sys.stdin.readline().rstrip('\n').split('/')
        line.pop(0)
        exist.add_rec(line, 0)
    #print ncreate
    nbmkdir = 0
    #print exist
    for n in range(ncreate):
        #create.append(sys.stdin.readline().rstrip('\n'))
        line = sys.stdin.readline().rstrip('\n').split('/')
        line.pop(0)
        nbmkdir += exist.add_rec(line, 0)
        #print exist
    #print create
    print "Case #" + str(i+1) + ": " + str(nbmkdir)
