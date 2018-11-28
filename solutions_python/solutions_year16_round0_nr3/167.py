import random
t = raw_input()
n, j = map(int, raw_input().split())

lim = [3, 2, 5, 2, 7, 2, 3, 2, 11]

def dv(k, p):
  i = 2
  while i * i <= k and i <= 50:
    if k % i == 0:
      return i
    i += 1
  return None

print 'Case #1:'

output = []

for i in xrange(1 << (n-1)):
  if i % 2 == 0:
    continue
  if random.random() < 0.98:
    continue
  ans = []
  s = "{0:b}".format(i + (1 << (n-1)))
  #print 'test', s
  for p in xrange(2, 11):
    res = dv(int(s, p), p)
    ans.append(res)
    if res == None:
      break
  if ans[-1] == None:
    continue
  output.append((s, ans))
  #print len(output), s

  if len(output) == j:
    break

for entry in output:
  print entry[0], ' '.join(map(str, entry[1]))
