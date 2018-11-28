import sys
FNAME = sys.argv[1] #"sample.in.txt"


def ncalls(ftree, targets):
    return 0

class node(object):
    def __init__(self, fn):
        self.name = fn
        self.children = []

    def containsdir(self, d):
        return d in [i.name for i in self.children]

    def getdir(self, d):
        l = [i.name for i in self.children]
        i = l.index(d)
        return self.children[i]

    def __repr__(self):
        s = "[" + self.name + " ("
        s += ",".join([i.__repr__() for i in self.children])
        return s + ")]"

def addpathtotree(atree, newfile):
    assert(newfile[0] == '/')

    count = 0
    pwd = atree

    for pathpart in newfile.split("/")[1:]:
        if pwd.containsdir(pathpart):
            # go there, don't increment. no call to mkdir
            pass
        else:
            newnode = node(pathpart)
            pwd.children.append(newnode)
            count += 1
        pwd = pwd.getdir(pathpart)
    return count
        
            
        
        



if __name__ == "__main__":
    
    # a = node("/")
    # print "a: ", a
    # print addpathtotree(a, "/asdf/asdf")
    # print addpathtotree(a, "/qwerty")
    # print addpathtotree(a, "/qwerty")
    # print a

    
    f = open(FNAME)
    flines = f.readlines()
    T = int(flines.pop(0))
    testi = 1
    while len(flines):
        N, M = map(int, flines.pop(0).split())

        existing = []
        targets = []
        root = node("/")
        for i in range(N):
            existing.append(flines.pop(0).strip())
            addpathtotree(root, existing[-1])
        # print root
        # print
        
        totalcount = 0
        for i in range(M):
            targets.append(flines.pop(0).strip())
            totalcount += addpathtotree(root, targets[-1])

        print "Case #" + str(testi) + ":", totalcount
        testi += 1
