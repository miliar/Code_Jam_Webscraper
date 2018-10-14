import sys

data = sys.stdin.readlines()
t = int(data[0])
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[i+1].split()

    n = [int(c) for c in d[0]]
    
    for j in range(1, len(n))[::-1]:
        if n[j] < n[j-1]:
            for k in range(j, len(n)):
                n[k] = 9
            n[j-1] -= 1

    s = ""
    if n[0] is not 0:
        s += str(n[0])
    for j in range(1, len(n)):
        s += str(n[j])
    
    print s
