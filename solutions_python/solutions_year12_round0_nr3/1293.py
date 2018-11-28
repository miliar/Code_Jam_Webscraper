import sys
T = int(sys.stdin.readline().strip())
for c in range(1, T+1):
    allsets = set()
    (a, b) = sys.stdin.readline().strip().split()
    (a, b) = (int(a), int(b))
    for i in range(a, b+1):
        s = str(i)
        l = len(s)
        for j in range(1, l):
            recycled = int(s[l-j:l] + s[0:l-j])
            if recycled > i and recycled <= b: 
                allsets.add((i, recycled))
                allsets.add((recycled, i))
    
    print "Case #%d: %d" % (c, len(allsets)/2)
