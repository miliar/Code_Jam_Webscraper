#!/usr/bin/python

import sys

class Solution():
  visited = {}

def max_min(arr, n):
  i = 0
  curr_max = [-1, []]
  while i < n:
    if i not in Solution.visited:
      if curr_max[0] < min(arr[i][0], arr[i][1]):
        curr_max[0] = min(arr[i][0], arr[i][1])
        curr_max[1] = [i]
      elif curr_max[0] == min(arr[i][0], arr[i][1]):
        curr_max[1].extend([i])
    i = i + 1
  return curr_max
     
def get_index(arr, curr_max):
  lst = []
  max_max = -1
  min_index = sys.maxint
  len1 = len(curr_max[1])

  if len1 == 1: 
    return curr_max[1][0]
  elif len1 > 1:
    for index in curr_max[1]:
      if max(arr[index][0], arr[index][1]) > max_max:
        max_max = max(arr[index][0], arr[index][1])
        lst = [index]
      elif max(arr[index][0], arr[index][1]) == max_max:
        lst.extend([index])
    if len(lst) == 1:
      return lst[0]
    elif len(lst) > 1:
      for index in lst:
        if index < min_index:
          min_index = index
      return min_index
       
def update_val(arr, index, n):
  i = index - 1
  j = index + 1

  while i >= 0 and i not in Solution.visited:
    arr[i][1] = index - i - 1
    i = i - 1

  while j < n and j not in Solution.visited:
    arr[j][0] = j - index - 1
    j = j + 1

  return arr
  

def bath(n, k):
  i = 0
  arr = []
  while i < n:
    arr.append([(i - 0), (n - 1 - i)])
    i = i + 1

  while k > 0:
    curr_max = max_min(arr, n)
    index = get_index(arr, curr_max)
    Solution.visited[index] = 1
    x = arr[index][1]
    y = arr[index][0] 
    arr = update_val(arr, index, n)
    k = k - 1
      
  return(x, y) 
  

def main():
  t = int(raw_input())
  for i in xrange(1, t+1):
    n, k = [int(x) for x in raw_input().split(" ")]
    Solution.visited = {}
    (x, y) = bath(n, k)
    print "Case #%d: %d %d" % (i, x, y)

if __name__ == '__main__':
  main()


