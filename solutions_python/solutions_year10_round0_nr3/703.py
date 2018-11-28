import sys

p_stdin = sys.stdin
p_stdout = sys.stdout

sys.stdin = file('C-small-attempt0.in', 'rt')
#sys.stdin = file('C-large.in', 'rt')
sys.stdout = file('C-small-attempt0.out', 'wt')
#sys.stdout = file('C-large.out', 'wt')

t = int(raw_input())

for _ in xrange(t):
    l = raw_input().split()
    R = int(l[0])
    k = int(l[1])
    N = int(l[2])

    gs = raw_input().split()
    gs = [int(v) for v in gs]
    
    s = []
    for i in range(N):
        j = i
        c = 0
        x = 0
        while True:
            if x >= N or c + gs[j] > k:
                s.append((c, j))
                break;
            else:
                c += gs[j]
                j = (j + 1) % N
                x += 1

    p = 0
    cg = 0
    for r in xrange(R):
        p += s[cg][0]
        cg = s[cg][1]

    print "Case #%d: %d" % (_+1, p)

sys.stdin.close()
sys.stdout.close()

sys.stdin = p_stdin
sys.stdout = p_stdout
