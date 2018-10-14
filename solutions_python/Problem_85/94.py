import sys

f = open(sys.argv[1], 'r')

T = int(f.readline())

for t in xrange(T):
  line = [int(x) for x in f.readline().strip().split(' ')]
  L, tt, N, C = line[:4]
  a = line[4:] * (N / C)
  g = 0
  for i in xrange(len(a)):
    if sum(a[:i]) * 2 >= tt:
      g = i
      break
  a += a[:N % C]
  a = a[:g] + list(reversed(sorted(a[g:])))
  
  time = 0
  for i, d in enumerate(a):
    build_time = max(0, tt - time)
    if build_time < 2 * d and build_time > 0:
      if L > len(a) - g or (i < len(a) and (d - build_time * 0.5) > a[i + 1]):
        time += build_time + (d - build_time * 0.5)
        L -= 1
      else:
        time += d * 2
    elif L > 0 and build_time < 2 * d:
      time += build_time + (d - build_time * 0.5)
      L -= 1
    else:
      time += d * 2
      
  print 'Case #%d:' % (t + 1), int(time)

f.close()
