import sys
import numpy as np
import math
import heapq

def small_2(l):
    if l[1][1] - l[0][0] <= 720 or l[0][1] + 2*720 - l[1][0] <= 720:
        return 2
    else:
        return 4

def small(cameron, jamie):
    cameron.sort()
    jamie.sort()
    if len(cameron) == 1 and len(jamie) == 0:
        return 2
    if len(cameron) == 0 and len(jamie) == 1:
        return 2
    if len(cameron) == 1 and len(jamie) == 1:
        return 2
    if len(cameron) == 2 and len(jamie) == 0:
        return small_2(cameron)
    if len(jamie) == 2 and len(cameron) == 0:
        return small_2(jamie)
    
T=int(sys.stdin.readline())
for t in range(1, T+1):
    line=sys.stdin.readline()
    [Ac, Aj]=map(int, line.split())
    cameron = []
    for _ in range(Ac):
        line=sys.stdin.readline()
        [Ci, Di]=map(int, line.split())
        cameron.append((Ci, Di))
    jamie = []
    for _ in range(Aj):
        line=sys.stdin.readline()
        [Ci, Di]=map(int, line.split())
        jamie.append((Ci, Di))
    
    #print("cameron=", cameron, "jamie=", jamie)
    res = small(cameron, jamie)
    print("Case #%d: %d" % (t, res))
