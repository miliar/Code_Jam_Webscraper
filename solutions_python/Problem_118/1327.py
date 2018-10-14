import math
import time
start_time = time.time()

def is012exist(snum):
  return True
  lst = ['0', '1', '2']
  if snum[0] not in lst:
    return False
  for i in snum:
    if i not in lst:
      return False
  return True

def ispaliandrom(num):
  nums = str(num)
  if nums[0] == nums[-1]:
    num = list(nums)
    num.reverse()
    return nums == ''.join(num)
  return None

lst = ['0', '1', '2']

def getList(pow):
  pow = int(pow / 2)
  defaultList = [[1, 1], [2, 4], [3, 9]]
  last = 10 ** pow
  rng = [[11, 22, 1]]
  for i in range(1, pow - 1):
    ns = lst[1] + lst[0] * i + lst[1]
    rng.append([int(ns), int(lst[1] + lst[2] * i + lst[1]), 10])
    ns = lst[2] + lst[0] * i + lst[2]
    x = int(ns)
    if len(ns) % 2 == 0:
      rng.append([x, x, 1])
    else:
      rng.append([x, int(lst[2] * (i + 2)), 10 ** int(len(ns) / 2)])
#  print rng
  for r in rng:
    for i in range(r[0], r[1] + 1, r[2]):
      isi = ispaliandrom(i)
      if isi:
        square = i * i
        if ispaliandrom(square):
          defaultList.append([i, square])
  return defaultList

def countsquare(x=0, y=0):
  fp = open('C-small-attempt.in', 'r')
  n = fp.readline().strip('\r\n')
  counters = []
  j = 1
  for line in fp:
    x, y = line.strip('\r\n').split(' ')
    x = int(x)
    count = 0
    lny = len(y)
    y = int(y)
#    print x, y
#    print lny
    for i in getList(lny):
#      print i
      if i[1] >= x and i[1] <= y:
        count += 1
    counters.append('Case #%s: %s' % (j, count))
    j += 1
  return counters

xy = countsquare()
print xy
fp = open('C-small-attempt_out.txt', 'w')
fp.write('\n'.join(xy))
fp.close()
print time.time() - start_time, "seconds"
