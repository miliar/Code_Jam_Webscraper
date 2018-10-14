"""
Created on Sat Apr  8 09:19:27 2017
@author: Data Luu
GCJ 2017 - R0 - P1
"""
import math
a = 10
N = 6
K = 2
def solve(N, K):
    base = 2 ** math.floor(math.log(K,2)) - 1
    dis = (N-base) // (base + 1)
    more = (N - base) % (base + 1)
    if K - base <= more:
        return (math.ceil(dis/2), math.floor(dis/2))
    else:
        return (math.ceil((dis-1)/2), math.floor((dis-1)/2))
with open("in","r") as reader:
    with open("out",'w') as writer:
        t = int(reader.readline())
        for i in range(t):
            N, K = map(int, reader.readline().split())
            mx, mn = solve(N,K)
            writer.write("Case #" + str(i+1) + ": " + str(mx) + " " + str(mn) + "\n")
