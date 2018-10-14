import sys

sys.stdin = open("A-large.in", 'r')
sys.stdout = open("A-large.out", 'w')

t = int(raw_input())

for asd in xrange(t):
    d,n = map(int,raw_input().split())
    pos = []
    spd = {}
    for i in xrange(n):
        si,vi = map(float, raw_input().split())
        pos.append(si)
        spd[si] = vi

    pos = list(reversed(sorted(pos)))

    maxT = 0
    #minV = spd[pos[0]]
    
    for i in xrange(n):
        maxT = max(maxT, (d-pos[i])/spd[pos[i]] )

    print "Case #"+str(asd+1)+":",
    print format(d/maxT, ".6f")

sys.stdin.close()
sys.stdout.close()
