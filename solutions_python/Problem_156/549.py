import sys

args = sys.argv
file = args[1]
f = open(file)

cases = int(f.readline())

def special(a,n):
    return sum([(x-1)/n for x in a])

for i in range(cases):
    D = int(f.readline())
    P = [int(x) for x in f.readline().split(' ')]
    m = special(P,1) + 1
    for j in range(max(P) + 1)[1:]:
        mn = special(P, j)
        if (mn + j) < m:
            m = mn + j
        if m < j:
            break;    
    print "Case #%s: %s" % (i + 1,m)
    
