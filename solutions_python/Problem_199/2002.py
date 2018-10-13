import sys
import math
from collections import deque
import sets
import itertools
import copy

def swap_if_possible(s, i, k):
    #print "sip", s, i, k
    cant = False
    for j in range(i, i+k):
        if j >= len(s):
            return False
        if s[j] != '-':
            cant = True
            break

    if not cant:
        for j in range(i, i +k):
            s[j] = '+'
        return True

    return False

def remove_obvious(s, k):
    i = 0
    swaps = 0
    while i <= len(s)-k:
        if s[i] == '-':
            if swap_if_possible(s, i, k):
                #print "ss"
                swaps += 1
        i += 1

    while len(s) > 0:
        if s[0] == '-':
            break
        else:
            #print "me!!", s[0], s
            del s[0]

    while len(s) > 0:
        if s[len(s)-1] == '-':
            break
        else:
            #print "me!"
            del s[len(s)-1]

    return swaps

def swap(s, i, k):
    for j in range(i, i+k):
        if s[j] == '-':
            s[j] = '+'
        else:
            s[j] = '-'

def dfs(s, k, num):
    #print "beforeobv", s
    num += remove_obvious(s, k)
    #print "remobv", s, num
    if len(s) == 0:
        return num
    if len(s) < k:
        return -1
    #print "afterobv", s
    i = 0
    while i < len(s)-k:
        if s[i] == '-':
            swap(s, i, k)
            num += 1
            num = dfs(s, k, num)
            #print "dfs", s, num
            if num >= 0:
                return num
            else:
                return num
            i += 1

    #print "opop!!!!!!!!!!"
    return -2
            
            
def solve(s, k):
    #swaps = remove_obvious(s, k)
    num = 0
    return dfs(s, k, num)

T = int(sys.stdin.readline().strip())
for i in range(0, T):
    s, ks = sys.stdin.readline().split()
    k = int(ks)
    res = solve(list(s), k)
    if res >= 0:
        print "Case #"+str(i+1)+": "+ str(res)
    else:
        print "Case #"+str(i+1)+": IMPOSSIBLE"

#s = ['+', '-', '-', '-']
#print remove_obvious(s, 3)
#print s
