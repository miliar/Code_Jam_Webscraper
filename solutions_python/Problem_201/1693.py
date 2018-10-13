
fout = open('BathroomStalls-small1gcj.out', 'w')

def lp(s, n):
    return (n-len(s))*'0'+s

def doprint(s):
    print(s)
    fout.write(s+'\n')

def close():
    fout.close()


import heapq
import math

class MyHeap(object):
   def __init__(self, initial=None, key=lambda x:x):
       self.key = key
       if initial:
           self._data = [(key(item), item) for item in initial]
           heapq.heapify(self._data)
       else:
           self._data = []

   def push(self, item):
       heapq.heappush(self._data, (self.key(item), item))

   def pop(self):
       return heapq.heappop(self._data)[1]

# PriorityQueue Question

# while numremoved < K...
#   split all the ones at the head of the pq


T = int(input())


for tc in range(1,T+1):
    h = []
    
    N, K = list(map(int, input().split()))

    heapq.heappush(h, (-N, N, 1))

    lside = 0
    rside = 0

    nremoved = 0
    while nremoved < K:
        ncanremove = h[0][2]
        ntoremove = min(K-nremoved, ncanremove)
        
        cnum = h[0][1]
        
        #h[0][2] -= ntoremove
        if ntoremove == ncanremove: #h[0][2] == 0:  # !!! this will leave it incorrect for the last one
            heapq.heappop(h)

        if ntoremove > 0: # always
            lside = math.floor((cnum-1)/2.0)
            rside = math.ceil((cnum-1)/2.0) # or reversed lside and rside
            heapq.heappush(h, (-lside, lside, ntoremove))
            heapq.heappush(h, (-rside, rside, ntoremove))

            nremoved += ntoremove

            #print(h)

    #ans = str(h[0][1]) + " "+ str(heapq.nlargest(1, h)[0][1])
    #print(h)
    ans = str(max(lside, rside)) + " " + str(min(lside, rside))
    
    doprint("Case #"+str(tc)+": "+str(ans))

close()

'''
4
9 1
100 1
1000 1
10 2
'''

'''
4
5000 5000
90000 30000
900000 500000
900000 400000
'''

'''
3
4 2
5 2
6 2
'''

'''
5
4 2
5 2
6 2
1000 1000
1000 1
'''
