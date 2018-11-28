def isDone(pencakes):
  for p in pencakes:
    if p == '-':
      return False
  return True

def pencake_sorting(pencakes, cnt):
  answer = 0
  pencakes = list(pencakes)
  while not isDone(pencakes):
    for i in range(len(pencakes)):
      if pencakes[i] == '-':
        for j in range(cnt):
          if i+j >= len(pencakes):
            return "IMPOSSIBLE"
          if pencakes[i+j] == '-':
            pencakes[i+j] = '+'
          else:
            pencakes[i+j] = '-'
        answer = answer + 1 
  return answer 

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()
  pencakes = n.split(' ')[0]
  cnt = int(n.split(' ')[1])
  res = pencake_sorting(pencakes, cnt)
  print "Case #{}: {}".format(i, res)
