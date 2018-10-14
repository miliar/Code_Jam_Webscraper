#!/usr/bin/python

from sys import stdin

def main():
    numsamples = int(stdin.readline())
    for i in range(1, numsamples + 1):
        puzz = readpuzzle()
        d = deceitful(puzz)
        h = honest(puzz)
        print "Case #%d: %d %d" % (i, d, h)

def deceitful(puzz):
    score = 0
    n, k = puzz
    naomi = n[:]
    ken = k[:]
    while len(naomi) > 0 and naomi[-1] > ken[0]:
        to_beat = ken.pop(0)
        for i in range(len(naomi)):
            if naomi[i] > to_beat:
                naomi.pop(i)
                score += 1
                break
    return score

def honest(puzz):
    score = 0
    n, k = puzz
    naomi = n[:]
    ken = k[:]
    while len(naomi) > 0:
        chosen = naomi.pop()
        index = len(ken) - 1
        if chosen > ken[-1]:
            score += 1
            ken.pop(0)
        else:
            found = False
            for i in range(len(ken)):
                if ken[i] > chosen:
                    ken.pop(i)
                    found = True
                    break
            if not found:
                ken.pop(0)
    return score

def readpuzzle():
    num_blocks = int(stdin.readline())
    naomi = stdin.readline().strip()
    naomi = [float(block) for block in naomi.split(" ")]
    naomi.sort()
    ken = stdin.readline().strip()
    ken = [float(block) for block in ken.split(" ")]
    ken.sort()
    return (naomi, ken)

if __name__ == "__main__":
    main()
