import sys
import math

def good_not_surprising(target, score):
    base = (score + 2) / 3
    return base >= target

def good_surprising(target, score):
    if score % 3 == 0:
        return (score >= 3) and ((score / 3) + 1 >= target)
    elif score % 3 == 1:
        return (score >= 4) and ((score / 3) + 1 >= target)
#    elif score % 3 == 2:
    else:
        return (score >= 2) and ((score / 3) + 2 >= target)

def solve(n, s, target, scores):
    simples = filter(lambda x: good_not_surprising(target, x), scores)
    todo = filter(lambda x: not good_not_surprising(target, x), scores)
    surprisings = filter(lambda x: good_surprising(target, x), todo)
#    print simples, surprisings
    return len(simples) + min(len(surprisings), s)

with file(sys.argv[1], 'r') as f:
    l = f.readlines()
    n = int(l[0].rstrip())
    for i in xrange(1, n + 1):
        vals = map(int, l[i].rstrip().split(' '))
        print "Case #%d: %d" % (i, solve(vals[0], vals[1], vals[2], vals[3:]))

