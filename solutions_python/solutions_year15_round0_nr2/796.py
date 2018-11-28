
import collections
import math
from heapq import heapify, heappush, heappop
from heapq import _heapify_max as mheapify
from heapq import _siftdown_max, _siftup_max

def mheappush(heap,item):
    heap.append(item)
    _siftdown_max(heap,0,len(heap)-1)

def mheappop(heap):
    lastegt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastegt
        _siftup_max(heap,0)
    else:
        returnitem = lastegt
    return returnitem


def heuristic(a):
    return a[0]

def neighbors(a):
    ret = []
    ret.append(s1(a))
    m = mheappop(a)
    for i in range(2,m/2+1):
        t = [x for x in a]
        mheappush(t,i) #s2
        mheappush(t,m-i)
        ret.append(t)
    #print ret
    return ret
        
    
def s1(a):
    ret = map(lambda x:max(x-1,0),a)
    mheapify(ret)
    return ret



def solve(a):
    mheapify(a)
    fringe = []
    heappush(fringe,(0,a))

    known = {}
    known[tuple(a)] = 0

    ret = 10000   
    while len(fringe) > 0:

        _,current = heappop(fringe)
        #print known[tuple(current)],current
        if heuristic(current) == 0:
            v = known[tuple(current)]
            if v < ret: ret = v
            continue

        c = known[tuple(current)] + 1
        for n in neighbors(current):
            t = tuple(n)
            if not t in known or c < known[t]:
                heappush(fringe,(c + heuristic(n),n))
                known[t] = c

    return ret
    

t = int(raw_input())

for i in range(0,t):
    D = int(raw_input())
    diners = map(int,raw_input().split(" "))


    
    

    

    print "Case #%d: %d" %(i+1,solve(diners))

"""
10
|\
3 7
  |\
  3 4

Given N stacks of pancakes with max height H, the minimum time required will be H / 2 + 1; H/4+3; H/8+7; H/16+

H / 2 + num_stacks; => num_stacks[H/2] += 2 * num_stacks[H]

i = highest_stack
while(i > 0):

    {stack heights | stack_height / 2 <= magnitude(.)}
    i -= 1


1 -> 0 (1)
2 -> 1 -> 0 (2)
3 -> [2,1] -> [1,0] -> [0,0] (3)
4 -> [2,2] -> [1,1] -> [0,0] (3)
5 -> [2,3] -> [1,2] -> [0,1] -> [0,0] (4)
6 -> [3,3] -> [2,2] -> [1,1] -> [0,0] (4)
7 -> [4,3] -> [2,2,3]... (5)
8 -> [4,4] -> [2,2,4] -> [2,2,2,2] -> [1,1,1,1] -> [0,0,0,0] (5)
9 -> [6,3] -> [3,3,3] -> [2,2,2] -> [1,1,1] -> [0,0,0] (5)
10 -> [5,5] -> 4,4; 3,3; 2,2; 1,1; 0,0
11 -> 3,8; 3,4,4; (6)
11 -> 5,6; (7)


L = a + b + c + ... such that max({a,b,c,...}) <= L - ||{a,b,c,...}||

10, 7, 7, 7, 7, 7
[7,3,7,7,7,7,7,7]

10, 10, 7
5, 5, 10, 7
5, 5, 5, 5, 7
6...


20, 20, 18

Is the time taken to halve all large pancake stacks less than the time required to consume n/2 pancakes?

Halve all pancake stacks larger than n/2

if next biggest number is less than biggest number - magnitude(biggest number) - 1

[10], [5,5], [4,4], [3,3], [2,2], [1,1] [0,0]
[10], [3,7], [3,3,4],
[10], [5,5], [3,2,5]

[32], [16,16], [16, 8, 8], [8, 8, 8, 8], is ceil(n/2) > count(l > n/2)?
"""
