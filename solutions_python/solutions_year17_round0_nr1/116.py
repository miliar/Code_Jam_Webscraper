

from copy import deepcopy



def solve(s,k):
  num=str2num(s)
  count = 0
  xor_val = 2**k-1
  while num >= 2**(k-1):
    if num & 1:
      num = num ^ xor_val
      count += 1
    num = num // 2
    #print(num)
  #return (num,count)
  if num == 0:
    return count
  else:
    return -1
      


def str2num(s):
  num = 0
  for i in range(len(s)):
    num = 2*num
    if s[i] == '-':
      num+=1
  return num
      


if __name__ == "__main__":
  t = int(input())
  for i in range(1, t + 1):
    s,num = [s for s in input().split(" ")]
    k = int(num)
    res = solve(s,k)
    if res == -1:
      print("Case #{}: IMPOSSIBLE".format(i))
    else:
      print("Case #{}: {}".format(i, res))




