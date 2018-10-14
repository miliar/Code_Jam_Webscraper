import io
import sys

sample = """\
1
1 1
/a
/b
"""

#fin = io.StringIO(sample)
#fout = sys.stdout
fin = open("A-small-attempt4.in")
fout = open("A-small-attempt4.out", "w")
#fin = open("A-large-practice.in")
#fout = open("A-large-practice.out", "w")

readLine = lambda : fin.readline().strip()
readInt = lambda : int(readLine())
readIntList = lambda : [int(x) for x in readLine().split()]

nofCases = readInt()

def add(d):
    x = d.split("/")[1:]
    p =  tree
    for e in x:
        if e not in p:
            p[e] = {}
        p = p[e]

    
def create(d):
    if d == "/":
        return 0
    r = 0
    #print d
    x = d.split("/")[1:]

    p =  tree
    for e in x:
        if e not in p:
            p[e] = {}
            r += 1
            #print "toadd", e
        p = p[e]

    return r
    

for tc in range(1, nofCases + 1):
    N, M = readIntList()

    
    tree = {}
    for i in range(N):
        d = readLine()
        #print "exist:", d
        add(d)

    ans = 0
    for i in range(M):
        d = readLine()
        #print "toadd", d
        ans += create(d)

    print >> fout, "Case #%d: %d" % (tc, ans)


if fout != sys.stdout:
    fout.close()

