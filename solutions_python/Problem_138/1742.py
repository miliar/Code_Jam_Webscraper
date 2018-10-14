#!/usr/local/bin/python3.2
from sys import *

num = stdin.readline()
num = int(num)

def war(n, naomi, ken):
    i_naomi = i_ken = 0
    while i_naomi < n and i_ken < n:
        while i_ken < n and ken[i_ken] < naomi[i_naomi]:
            i_ken += 1
        if i_ken == n:
            break
        else:
            i_naomi += 1
            i_ken += 1
    return n - i_naomi

def dwar(n, naomi, ken):
    naomi_s = 0
    ken_s = 0
    score = 0
    while naomi_s < n:
        if naomi[naomi_s] > ken[ken_s]:
            score += 1
            naomi_s += 1
            ken_s += 1
        else:
            naomi_s += 1
    return score

for c in range(1, num+1):
    n = int(stdin.readline())
    naomi = [float(x) for x in stdin.readline().split()]
    ken = [float(x) for x in stdin.readline().split()]
    naomi.sort()
    ken.sort()
    ws = war(n, naomi, ken)
    dws = dwar(n, naomi, ken)
    print("Case #%d: %d %d" % (c, dws, ws))

    
