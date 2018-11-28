T = int(input())
for testcase in range(1, T + 1):
  s, k = input().strip().split()
  k = int(k)
  cake = []
  for c in s:
    cake.append(1 if c == '+' else 0)
  ans = 0
  for i in range(len(cake) - k + 1):
    if cake[i] == 0:
      ans += 1
      for j in range(0, k):
        cake[i + j] = 1 - cake[i + j]
  if 0 in cake:
    ans = "IMPOSSIBLE"
  print("Case #{}: {}".format(testcase, ans))
  
