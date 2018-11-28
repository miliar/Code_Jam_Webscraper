import sys

sys.stdin = open("B-large.in", 'r')
sys.stdout = open("out.out", 'w')

def check(s, length):
  for i in range(length-1):
    if int(s[i]) > int(s[i+1]):
      return False
  return True

T = int(input())
for i in range(1, T+1):
  count = 0
  case = input()
  l = len(case)
  for j in range(l-1):
    if int(case[j]) >= int(case[j+1]):
      count = l-j-1
      break
  if check(case, l):
    ans = int(case)
  else:
    ans = ((int(case) // 10 ** count) * 10 ** count) - 1
  print("Case #{}: {}".format(i, ans))