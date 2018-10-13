# CodeJam!

class Data():
    pass

class Node():
    def __init__(self):
        self.children = {}

def solve(d):
    root = Node()
    for p in d.given:
        l = p.split('/')[1:]
        now = root
        for x in l:
            if x != '':
                if x not in now.children:
                    now.children[x] = Node()
                now = now.children[x]
    ans = 0
    for p in d.want:
        l = p.split('/')[1:]
        now = root
        for x in l:
            if x != '':
                if x not in now.children:
                    now.children[x] = Node()
                    ans += 1
                    #print "YEAH"
                now = now.children[x]
    return ans
    
def readdata():
    global fin, fout
    nt = int(fin.readline())
    #nt = 2
    for testnum in range(1, nt+1):
        d = Data()
        n, m = fin.readline().split()
        n = int(n)
        m = int(m)
        d.given = []
        d.want = []
        for i in xrange(n):
            d.given.append(fin.readline().strip())
        for i in xrange(m):
            d.want.append(fin.readline().strip())
        fout.write("Case #" + str(testnum) + ": " + str(solve(d)) + "\n")

def openfile(name):
    global fin, fout
    if name[-3:] == ".in": name = name[:-3]
    fin = open(name + ".in", 'r')
    fout = open(name + ".out", 'w')

def main(name):
    global fin, fout
    openfile(name)
    readdata()
    fin.close()
    fout.close()
    
