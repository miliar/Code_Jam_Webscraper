"""    LS    RS
xxxx
 .     1     2
 ..    0     1
xxxxx
  .    2     2
. .    0     1
xxxxxx
  .    2     3
  . .  1     1
LS <= RS
LS is equal to RS or one less
for N and K, take middle, is then partitioned into
(n-1)/2 floor and ceil
"""

import math
from queue import PriorityQueue

def left(i):
    return math.floor((i-1)/2)

def right(i):
    return math.ceil((i-1)/2)

def foo(N, K):
    q = PriorityQueue()
    q.put((-N, (N, left(N), right(N))))
    for i in range(K):
        pri, n = q.get()
        # print(n)
        l = left(n[0])
        r = right(n[0])
        q.put((-l, (l, left(l), right(l))))
        q.put((-r, (r, left(r), right(r))))
    return n[2], n[1]

T = int(input())
for _ in range(T):
    N, K = [int(s) for s in input().split(" ")]
    # print(foo(N, K))
    res = foo(N, K)
    print("Case #{}: {} {}".format(_+1, res[0], res[1]))