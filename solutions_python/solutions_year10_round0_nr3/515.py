cases = int(raw_input())
for i in range(cases):
  [r, k, n] = map(int, raw_input().split(' '))
  queue = map(int, raw_input().split(' '))
  revenue = 0
  for j in range(r):
    car = []
    cap = k
    p = 0
    for p in range(len(queue)):
      if cap >= queue[p]:
        cap -= queue[p]
        car.append(queue[p])
      else:
        break
    else:
      p = len(queue)+1
    queue = queue[p:]     
    revenue += sum(car)
    map(queue.append, car)
  print 'Case #%d: %d' % (i+1, revenue)
	
