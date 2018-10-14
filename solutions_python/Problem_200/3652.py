def tidy(n):
  s = list(str(n))
  f = -1
  for i in xrange(0, len(s)-1):
    if ord(s[i]) > ord(s[i+1]):
      f = i
      break
  if f != -1:
    s = s[:f] + [chr(ord(s[f]) - 1)] + ['9']*(len(s) - f - 1)
    return tidy(int("".join(s)))
  return n

with open("B-large.in") as f:
  nc = int(f.readline().strip())
  for c in range(0, nc):
    n = int(f.readline().strip())
    print("Case #{}: {}".format(c+1, tidy(n)))