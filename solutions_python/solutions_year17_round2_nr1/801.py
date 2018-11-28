t = int(input())
for i in range(1, t + 1):
  D, N = [int(s) for s in input().split(" ")]
  maxtime = 0
  for n in range(N):
    K,S = [int(s) for s in input().split(" ")]
    time = (D-K)/S
    if time > maxtime:
      maxtime = time
  print("Case #{}: {}".format(i,D/maxtime))