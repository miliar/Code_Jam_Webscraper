#!/usr/bin/env python3

def solve(A,N):
  N.sort()
  maxA = max(N)+1
  n = len(N)

  if(A==1):
    return n

  if(maxA < A):
    return 0

  table = [[0 for i in range(int(maxA+1))] for j in range(n+1)]


  for i in range(n):
    i = n - i - 1
    for a in range(A,maxA+1):
      if N[i] < a:
        table[i][a]=table[i+1][min(a+N[i],maxA)]
      else:
        price = 0
        na = a
        while na <= N[i]:
          na += (na-1)
          price += 1
        na = min(na + N[i],maxA)
        table[i][a]=min(table[i+1][a]+1,table[i+1][na]+price)
#  print(table)

  return table[0][A]

if __name__ == "__main__":
    T = int(input());
    for c in range(T):
        [A,_] = [int(i) for i in input().split()]
        N = [int(i) for i in input().split()]
        R = solve(A,N)
        print("Case #{}: {}".format(c+1,R))
