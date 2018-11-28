t = int(raw_input())

for i in xrange(1, t + 1):
  
  s, x = [v for v in raw_input().split(" ")]
  a = [c == "+" for c in s]
  
  k = int(x)
  result = 0
  impossible = 0

  for j in xrange(0, len(a)):
      if not a[j]:
        if j > len(a) - k:
            impossible = 1
        else:
            for w in xrange(j, j + k):
                a[w] = not a[w]
            result += 1

  if impossible == 1:
    print "Case #{}: {}".format(i, "IMPOSSIBLE")
  else:
    print "Case #{}: {}".format(i, result)