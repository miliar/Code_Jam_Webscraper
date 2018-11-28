import sys
for case_num in range(int(sys.stdin.readline())):
  times,cap,n = [int(num) for num in sys.stdin.readline().split()]
  groups = [int(num) for num in sys.stdin.readline().split()]
  grp_sum = reduce(lambda a, b: a + b,groups)
  next = [0]
  rem_cap = [cap]
  for i in range(len(groups)):
    if i > 0: 
      next.append(next[i - 1])
      rem_cap.append(rem_cap[i - 1] + groups[i - 1])
    while rem_cap[i] >= groups[next[i]]:
      rem_cap[i] -= groups[next[i]]
      next[i] = (next[i] + 1) % len(groups)
      if next[i] == i: break
  num_euros = 0
  start = 0
  i = 0
  while i < times:
    num_euros += cap - rem_cap[start]
    start = next[start]
    i += 1
    if i > 0 and start == 0: 
      num_euros *= times/i
      times %= i
      i = 0
  print 'Case #' + str(case_num + 1) + ': ' + str(num_euros)
