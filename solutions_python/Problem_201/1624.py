#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# author Ladislav Vrbsky
# Google Code Jam 2017
# Qualification round
# Problem C. Bathroom Stalls

import math

# returns string 'maxLR minLR'
def empty_neighbors(n,k):
  maxLR, minLR = -1, -1
  level = math.floor(math.log2(k))+1 #levels from 1 up for ks from 1 up
  # level gives a number about how many times the original n has been split in halfs - once per level
  # only a log2 will give a close estimate on values min and max, but not a precise one
  maxLR_above = n        // 2**(level-1)
  minLR_above = (n-2**(level-1)+1)// 2**(level-1)

  id_in_level = k - 2**(level-1) # starting from 0
  # print(n,'min',minLR_above,'max',maxLR_above)
  # print('level', level, ':', id_in_level, '>=?', n, '-', (minLR+1), '*', 2**(level),'+1')
  # print('level', level, ':', id_in_level, '>?', (n-level) - minLR * 2**(level))
  no_higher_value = n - (minLR_above+1) * 2**(level-1) +1
  # print(id_in_level, no_higher_value)
  if id_in_level < no_higher_value:
    maxLR = maxLR_above//2
    minLR = (maxLR_above-1)//2
  elif id_in_level >= no_higher_value: # from n - minLR * 2**(level-1) - (2**(level-1)-1)
    maxLR = minLR_above//2
    minLR = (minLR_above-1)//2
  return str(maxLR)+' '+str(minLR)

def main():
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    n,k = [int(inp) for inp in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, empty_neighbors(n,k)))

if __name__ == '__main__':
  main()