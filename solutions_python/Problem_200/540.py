import sys

def tidy(n):
  if n < 10:
      return n
  s = str(n)[1:]
  if all(value == "0" for value in s):
    return n - 1
  tmp = str(n)
  tmp = list(str(n))
  i = len(tmp) - 1
  carry = 0
  res = ""
  while i > 0:
    if int(tmp[i]) < int(tmp[i-1]):
      for j in range(i,len(tmp)):
        tmp[j] = "9"
      tmpno = int(tmp[i-1])-1
      tmp[i-1] = str(tmpno)
    i = i -1
  return int("".join(tmp))

name = "B-large"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

print T
for t in xrange(T):
    num = int(f.readline().strip())
    res = tidy(num)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
