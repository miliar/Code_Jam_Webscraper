import itertools as it
import math

from sys import argv

def _print(msg, f, stdout=True):
    f.write(msg + '\n')
    if stdout:
        print msg

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: {0} input-file'.format(argv[0])

    with open(argv[1], 'r') as f, \
           open(argv[1].rsplit('.')[0]+'.out', 'w') as o:
        N = int(f.readline())
        for case in xrange(N):
            C, F, X = map(float, f.readline().rstrip().split())
            cps = 2.0
            nfarms = max(0, int(X/C - cps/F))
            time = X/(cps+F*nfarms) + sum(C/(cps+F*i) for i in xrange(nfarms))
            _print('Case #{0}: {1:.7f}'.format(case+1, time), o, stdout=False)

