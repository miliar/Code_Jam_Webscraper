#f = open("/home/roy/in.txt")
f = open("/home/roy/Downloads/A-large.in")

lines = f.readlines()
count = int(lines[0])

#print "There are %s cases" % count

def intersect((A1, B1), (A2, B2)):
    if A1 > A2 and B1 < B2:
        return True
    if A1 < A2 and B1 > B2:
        return True
    return False
#count = 10
idx = 1
for i in range(0, count):
    line1 = lines[idx]
    idx = idx + 1

    N = int(line1)
    
    #print "There are %d lines" % N
    
    wires = []
    for n in range(0, N):
        line1 = lines[idx]
        idx = idx + 1
        [A, B] = [int(a) for a in line1.rstrip().split(" ")]
        wires.append((A, B))

    #print str(wires)
    
    ans = 0
    for m in range(0, N):
        for n in range(0, m):
            if intersect(wires[m], wires[n]):
                ans = ans + 1
    
    print "Case #%d: %s" % (i+1, str(ans))
