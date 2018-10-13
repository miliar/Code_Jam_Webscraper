import sys

f = open(sys.argv[1])
lines = iter(f)
n = int(lines.next())
for i in xrange(1, n+1):
  C, F, X = [float(x) for x in lines.next().split()]
  n = 0
  total_time = 0.0

  while True:
    wait_without_building = X/(n*F + 2)
    building_time = C/(n*F + 2)
    wait_with_building = building_time + X/((n+1)*F + 2)

    if wait_without_building <= wait_with_building:
      total_time += wait_without_building
      break
    else:
      total_time += building_time
      n += 1
  print 'Case #{}: {:.7f}'.format(i, total_time)
