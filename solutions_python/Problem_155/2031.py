import sys

lines = sys.stdin.read().split('\n')
T = int(lines.pop(0))

for tn, line in enumerate(lines):
    if not line: break
    line = line.split(' ')
    smax = int(line[0])
    s = map(int,line[1])
    #print smax, s
    n = 0
    i = 0
    a = 0
    while i<smax:
        #print i, ":", n, "standing"
        n += s[i]
        if n < i+1:
            a += i+1-n
            n += i+1-n
            #print "adding", a
        i += 1
    print "Case #%d:"%(tn+1), a
