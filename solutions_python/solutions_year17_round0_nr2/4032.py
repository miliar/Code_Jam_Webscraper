import math

def isTidy(n):
    ns = [int(d) for d in str(n)]
    for i in range(1,len(ns)):
        if ns[i - 1] > ns[i]:
            return (False, i)
    return (True, 0)

def lastTidy(n):
    while True:
        tid, p = isTidy(n)
        if(tid):
            return n       
        n = n - int(str(n)[p:]) - 1
        
    return 0

T = int(input())
for i in range(1, T + 1):
  n = int(input())
  print("Case #{}: {}".format(i, lastTidy(n)))