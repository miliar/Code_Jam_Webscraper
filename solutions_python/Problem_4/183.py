import sys

def MinScalarProduct(v1, v2):
    v1.sort()
    v2.sort(reverse=True)
    
    res = 0
    for i in range(0, len(v1)):
        res += (v1[i] * v2[i])
        
    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

fin = open(sys.argv[1], "r")
inCases = int(fin.readline().strip())

for i in range(1, inCases + 1):
    n = int(fin.readline().strip())

    vs1 = fin.readline().strip()
    vs1 = vs1.split()
    v1 = []
    for x in vs1:
        v1.append(int(x))
        
    vs2 = fin.readline().strip()
    vs2 = vs2.split()
    v2 = []
    for x in vs2:
        v2.append(int(x))

    print "Case #%d: %s" % (i, MinScalarProduct(v1, v2))
