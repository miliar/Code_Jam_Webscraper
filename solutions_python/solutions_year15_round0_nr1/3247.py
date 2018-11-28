import sys

def solve():
   sm, ls = sys.stdin.readline().split()
   sm = int(sm)
   ts = 0
   ans = 0
   for i in range(sm + 1):
      if ts >= i:
         ts += int(ls[i])
      else:
         k = i - ts
         ts += k + int(ls[i])
         ans += k
   return str(ans)

T = int(sys.stdin.readline())
for t in range(T):
    print("Case #" + str(t + 1) + ": " + solve())
