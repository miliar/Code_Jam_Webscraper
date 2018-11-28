import sys

sys.stdin = open('snap.in.txt', 'r')
sys.stdout = open('snap.out.txt', 'w')

T = input('')

for t in xrange(T):
    N,K = map(int, raw_input('').split())

    if (K+1) % 2**N == 0:
        print 'Case #%d: ON' % (t+1,)
    else:
        print 'Case #%d: OFF' % (t+1,)

sys.stdin.close()
sys.stdout.close()
