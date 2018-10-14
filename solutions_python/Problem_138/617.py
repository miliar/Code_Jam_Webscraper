import sys
import bisect

lines = sys.stdin.readlines()

cases = int(lines[0])

lines = lines[1:]

def naomi_score(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    score = 0
    for i in range(len(naomi)):
        pos = bisect.bisect(ken, naomi[i])
        if pos == len(ken):
            score += 1
            ken = ken[1:]
        else:
            del ken[pos]
    return score

def naomi_score2(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    score = 0
    for i in range(len(naomi)):
        pos = bisect.bisect(ken, naomi[i])
        if pos == 0:
            del ken[-1]
        else:
            score += 1
            ken = ken[1:]
    return score

for t in range(cases):
    lines = lines[1:]
    naomi = map(float, lines[0].split())
    ken = map(float, lines[1].split())
    naomi.sort()
    ken.sort()
    fair_score = naomi_score(naomi, ken)
    score = naomi_score2(naomi, ken)
    print "Case #%d: %d %d" % (t+1, score, fair_score)
    lines = lines[2:]

    
