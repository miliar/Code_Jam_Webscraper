t = int(raw_input())
for i in range(1, t + 1):
  a, b, k = [int(x) for x in raw_input().split()]

  c = 0
  for j in range(0, a):
    for m in range(0, b):
      if j & m < k:
        c += 1

  print "Case #%d: %d" % (i, c)
