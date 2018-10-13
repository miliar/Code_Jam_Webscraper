import fileinput
import re
import sys
sys.setrecursionlimit(100000)

WHITESPACE = re.compile("\s+")

def readlines():
    for line in fileinput.input():
        yield map(float, WHITESPACE.split(line.strip()))




def ken(weights, naomi_weight):
    bigger_weight  = [
        weight
        for weight in weights
        if weight > naomi_weight
    ]
    #print bigger_weight
    if bigger_weight:
        return min(bigger_weight)
    else:
        return min(weights)


def naomi_cheating(weights, ken_weights):
    if min(ken_weights) < max(weights):
        return (min(w for w in weights if w > min(ken_weights)), max(ken_weights)+0.000001)
    else:
        return (min(weights), max(ken_weights)-0.000001)
        

def naomi_real(weights, naomi_weights):
    return (weights[0], weights[0])


def count(naomi_weights, ken_weights, naomi):
    naomi_score = 0
    naomi_weights = sorted(naomi_weights)
    ken_weights = sorted(ken_weights)
    while naomi_weights:
        assert len(naomi_weights) == len(ken_weights)
        #print "question",naomi_weights, ken_weights
        (naomi_real, naomi_tell) = naomi(naomi_weights, ken_weights)
        #print "resp",naomi_real, naomi_tell
        ken_choice = ken(ken_weights, naomi_tell)
        naomi_weights.remove(naomi_real)
        ken_weights.remove(ken_choice)
        naomi_score += (ken_choice < naomi_real)
    return naomi_score



def problems():
    lines = readlines()
    (T, ) = lines.next()
    for p in xrange(int(T)):
        (N,) = lines.next()
        naomi_weights = lines.next()
        ken_weights = lines.next()
        assert len(naomi_weights) == len(ken_weights) == int(N)
        fair_score = count(naomi_weights, ken_weights, naomi_real)
        cheating_score = count(naomi_weights, ken_weights, naomi_cheating)
        print "Case #%i: %i %i" % (p+1, cheating_score, fair_score)


problems()

