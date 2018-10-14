import sys

lines = sys.stdin.readlines()
lines = [l[:-1] for l in lines]
T = int(lines[0])

for tc in range(1, T+1):
  num = lines[tc]

  # Scan from the back
  change_point = len(num)
  r = 9
  idx = len(num) - 1
  while idx >= 0:
    l = int(num[idx])
    if l > r:
      change_point = idx
      r = l - 1
    else:
      r = l
    idx -= 1

  if len(num) == 1 or change_point == len(num):
    ans = num
  else:
    ans = num[0 : change_point] + str(int(num[change_point]) - 1) + '9' * (len(num) - change_point - 1)
    if ans[0] == '0':
      ans = ans[1:]

  # Print answer
  print("Case #{0}: {1}".format(tc, ans))
