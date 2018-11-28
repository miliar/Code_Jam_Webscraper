from pprint import pprint
import sys

def earned(R, k, g):
    # simply simulate the rides
    earn = 0
    for r in xrange(R):
        kr = 0
        onCoaster = []
        while g:
            if kr + g[0] > k:
                break
            gr = g.pop(0)
            kr += gr
            onCoaster.append(gr)
        earn += kr
        g.extend(onCoaster)
    return earn

def solveCase(c, f, o):
    R, k, N = [int(x) for x in f.readline().strip().split()]
    g = [int(x) for x in f.readline().strip().split()]
    assert len(g) == N
    
    earn = earned(R, k, g)
    
    o.write("Case #%d: %s\n" % (c, earn))

if __name__ == '__main__':
    input = sys.argv[1]
    f = open(input, 'rb')
    o = open(input.split(".")[0] + "-out" + ".txt", 'wt')
    cases = int(f.readline())
    for c in xrange(cases):
        solveCase(c+1, f, o)
    f.close()
    o.close()
