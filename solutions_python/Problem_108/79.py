#!/usr/bin/env python3

def solve(I):
  n = int(I)
  L = []
  for _ in range(n):
    y = [int(x) for x in input().split()]
    y.append(-1)
    L.append(y) # [di,li,0]

  D = int(input())
  L.append([D,1,-1])
  L[0][2] = L[0][0]


  j = 0
  while j < len(L):
#    print(L)
    [di,li,best] = L[j]
    i = j+1
    reach = di+best

#    print(reach)

    if best < 0:
      return "NO"

    while L[i][0] <= reach:
      bt = min(L[i][0]-di, L[i][1])
      if L[i][2] < bt:
        L[i][2] = bt
      if i==n:
        return "YES"
      i = i + 1
    j = j + 1
  return "NO"


if __name__ == "__main__":
    T = int(input());
    for c in range(T):
        I = input()
        R = solve(I)
        print("Case #{}: {}".format(c+1,R))