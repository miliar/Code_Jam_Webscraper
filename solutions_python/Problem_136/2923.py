import sys
import itertools

def rline(f=str):
    return f(sys.stdin.readline())

def sline(f=str):
    return [ f(elem) for elem in rline().split(' ') ]

def test(price, rate, goal):
    prevGoal = None
    usedTime = 0.0
    for nb in itertools.count():
        curRate = 2.0 + nb * rate
        curGoal = goal / curRate + usedTime
        if prevGoal is not None and curGoal > prevGoal:
            return prevGoal
        prevGoal = curGoal
        usedTime += price / curRate

nbTest = rline(int)
for testNo in range(nbTest):
    [c, f, x] = sline(float)
    res = test(c, f, x)
    print(('\r%.2f' % ((testNo + 1) / nbTest * 100.0)), file=sys.stderr, end='')
    print('Case #%d: %.7f' % (testNo + 1, res))
print('', file=sys.stderr)