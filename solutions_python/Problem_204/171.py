from collections import defaultdict
from fractions import Fraction as F
from math import ceil

T = int(input().strip())

def getcurservs(ings, wperserving):
    rv = 0
    for i in range(len(ings)):
        rv = max(rv, ceil((ings[i][0]/1.1)/wperserving[i]))
    return rv
    
def eliminatelowings(ings, wperserving, curserv):
    rv = False
    for i in range(len(ings)):
        while len(ings[i]) > 0 and (ings[i][0]/0.9) < (wperserving[i] * curserv):
            rv = True
            ings[i].pop(0)
    return rv
            
def justright(ings, wpserving, curserv):
    rv = True
    for i in range(len(ings)):
        if len(ings[i]) == 0: return False
        needed = curserv * wpserving[i]
        rv = rv and ((needed * 0.9) <= ings[i][0] <= (needed * 1.1))
    return rv

for t in range(1, T+1):
    N, P = map(int, input().strip().split(' '))
    wperserving = list(map(int, input().strip().split(' ')))
    ings = []
    for i in range(N):
        ing = list(map(int, input().strip().split(' ')))
        ing.sort()
        ings.append(ing)
    
    matches = 0
    cs = getcurservs(ings, wperserving)
    done = False
    while True:
        while eliminatelowings(ings, wperserving, cs):
            if any([len(x) == 0 for x in ings]):
                done = True
                break
            cs = getcurservs(ings, wperserving)
        if done: break
        if justright(ings, wperserving, cs):
            for i in range(N):
                ings[i].pop(0)
            matches += 1
            if any([len(x) == 0 for x in ings]):
                done = True
                break
            cs = getcurservs(ings, wperserving)
        else:
            cs += 1
        if done: break
            
        
    print('Case #%d: %d' % (t,matches))
    