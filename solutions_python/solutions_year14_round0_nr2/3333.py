# Cookie Clicker Alpha
# Author: Kai Kang
import sys
sys.setrecursionlimit(999999)

NUM_OF_CASES = int(raw_input())
final_answers = []
CLICK_RATE = 2.0

def timeToGetNFarm(n, C, F):
    """
    Calculates the time needed to buy n farms
    """
    if n == 0:
        return 0
    else:
        return timeToGetNFarm(n-1, C, F) + C/(CLICK_RATE+F*(n-1))

def answerFromFixedFarm(C, F, X, farm):
    Tfarm = timeToGetNFarm(farm, C, F)
    return Tfarm + X/(CLICK_RATE+F*farm)

def answer(C, F, X):
    """
    C: cookies needed to buy a cookie farm
    F: a farm gives F cookies per second
    X: winning goal
    """
    min_time = float('inf')
    if int(X/C) == 0:
        return X/CLICK_RATE
    for farm in xrange(int(X/C)+1):
        result = answerFromFixedFarm(C, F, X, farm)
        if result < min_time:
            min_time = result
    return min_time

for i in xrange(NUM_OF_CASES):
    [C, F, X] = map(float, raw_input().split())
    final_answers.append(answer(C, F, X))

for i in xrange(NUM_OF_CASES):
    print "Case #%d: %.7f" %(i+1, final_answers[i])
