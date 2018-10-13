
def solve(N, S, p, nums):
  ret = 0
  for num in nums:
    if not num:
      if not p: ret += 1
      continue
    div, mod = divmod(num, 3)
    if mod in (1, 2):
      div += 1
    if div >= p:
      ret += 1
      continue

    if S and div == p-1 and mod in (0, 2):
      S -= 1
      ret += 1
      continue

  return ret

T = int(input())

for i in range(T):
  N, S, p, *nums = [int(x) for x in input().split()]
  print('Case #%d:' % (i+1), solve(N, S, p, nums))
