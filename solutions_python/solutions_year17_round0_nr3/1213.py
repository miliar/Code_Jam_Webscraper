from codejam import CodeJam

from math import log

def testcase(f):
    (N, K) = (int(i) for i in f.readline().split())
    rounds = int(log(K, 2))
    thisround = 2 ** rounds
    stallsleft = N - (thisround - 1)
    mindist = int(stallsleft / thisround)
    maxdist = mindist + 1
    nummax = stallsleft - (mindist * thisround)
    nummin = thisround - nummax
    if K - (thisround - 1) > nummax:
        span = mindist
    else:
        span = maxdist
    if span % 2:
        return '{0} {0}'.format((span-1)//2)
    else:
        return '{} {}'.format((span-1)//2 + 1, (span-1)//2)

cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
