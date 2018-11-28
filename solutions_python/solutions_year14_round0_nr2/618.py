for cas in range(int(raw_input())):
  c, f, x = [float(i) for i in raw_input().split()]
  s = [0.0 for i in range(int(max(c, f, x)))]
  for i in range(int(max(c, f, x))):
    s[i] = x / 2 if i == 0 else s[i - 1] - x / (2 + (i - 1) * f) + c / (2 + (i - 1) * f) + x / (2 + i * f)
  print "Case #%d: %.7f" % (cas + 1, min(s))
