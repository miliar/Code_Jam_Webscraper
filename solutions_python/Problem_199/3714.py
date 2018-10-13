# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import sys
import itertools
t = int(input())  # read a line with a single integer

def reverse(s):
  if s == '+':
    r = '-'
  else:
    r = '+'
  return r

def area_reverse(L, index, rg):
  if (len(L) - index) < rg:
    # 遡ってひっくり返す
    sti = (len(L) - index) - rg
    for k in range(sti, (sti + rg)-1):
      L[index+k] = reverse(L[index+k])
  else:
    # 普通にひっくり返す
    for k in range(0, rg):
      L[index+k] = reverse(L[index+k])

for i in range(1, t + 1):
  l = input().split(" ")  # read a list of integers, 2 in this case
  t_list = list(l[0])
  rgl = int(l[1])
  cnt = 0
  for j in range(0,len(t_list)):

    if t_list[j] == '-':
      area_reverse(t_list, j, rgl)
      cnt += 1
  if t_list.count('+') == len(t_list):
    result = cnt
  else:
    result = 'IMPOSSIBLE'
  print("Case #{}: {}".format(i, result))
