def solve(size, k):
  if (size <= 0):
    return (0, 0)

  if (k == 1):
    if (size%2 == 1):
      return ((size-1)//2, (size-1)//2)
    return (size//2, (size//2 -1))


  if (k%2 == 0):
    if (size%2 == 1):
      return solve((size-1)//2, k//2)
    else:
      return solve((size//2), k//2)
  else:
    if (size%2 == 1):
      return solve((size-1)//2, (k-1)//2)
    else:
      return solve(size//2 - 1, (k - 1)//2)


t = int(input())

for case in range(1, t + 1):
  n, k = map(int, input().split())
  l, r = solve(n,k)
  print("Case #" + str(case) + ":", l, r)
