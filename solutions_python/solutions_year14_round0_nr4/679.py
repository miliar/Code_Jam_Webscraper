import copy
  
T = int(raw_input())
for t in range(T):
  raw_input()
  a = sorted(map(float, raw_input().split()))
  b = sorted(map(float, raw_input().split()))
  new_a = copy.copy(a)
  new_b = copy.copy(b)
  score_1 = 0
  while len(a) > 0:
    tmp = a.pop()
    if tmp > max(b):
      b.pop(0)
      score_1 += 1
    else:
      for i in b:
        if i > tmp:
          b.remove(i)
          break
  a, b = new_a, new_b
  while all([i > j for i, j in zip(a, b)]) ==  False:
    b.pop()
    a.pop(0)
    
  print 'Case #%d:' % (t+1), len(a), score_1
