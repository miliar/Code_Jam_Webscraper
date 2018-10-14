import sys

lines = sys.stdin.readlines()
T = int(lines[0].rstrip())
for t in range(T):
    N = int(lines[3*t+1].rstrip())
    naomi = sorted(map(float, lines[3*t+2].rstrip().split(' ')))
    ken = sorted(map(float, lines[3*t+3].rstrip().split(' ')))
    wscore = 0
    while naomi != [] and ken != []:
        if naomi[-1] > ken[-1]:
            wscore += 1
            naomi, ken = (naomi[:-1], ken[1:])
        else:
            naomi, ken = (naomi[:-1], ken[:-1])
    naomi = sorted(map(float, lines[3*t+2].rstrip().split(' ')))
    ken = sorted(map(float, lines[3*t+3].rstrip().split(' ')))
    dscore = 0
    while naomi != [] and ken != []:
        if naomi[0] > ken[0]:
            dscore += 1
            naomi, ken = (naomi[1:], ken[1:])
        else:
            naomi, ken = (naomi[1:], ken[:-1])
    print "Case #%d: %d %d" % (t+1, dscore, wscore)
