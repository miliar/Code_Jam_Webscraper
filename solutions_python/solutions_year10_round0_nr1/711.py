import sys

p_stdin = sys.stdin
p_stdout = sys.stdout

#sys.stdin = file('A-small-attempt4.in', 'rt')
#sys.stdin = file('A-large.in', 'rt')
#sys.stdout = file('A-small-attempt4.out', 'wt')
#sys.stdout = file('A-large.out', 'wt')

t = int(raw_input())

for c in xrange(t):
    l = raw_input().split()
    n = int(l[0])
    k = int(l[1])

    on_p = pow(2, n) - 1
    if (k & on_p) == on_p:
        s = 'ON'
    else:
        s = 'OFF'

    print "Case #%d: %s" % (c+1, s)

sys.stdin.close()
sys.stdout.close()

sys.stdin = p_stdin
sys.stdout = p_stdout
