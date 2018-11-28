cache = {}

def load(name):
  f = file(name)
  s = f.readlines()
  f.close()
  for line in s:
    yield line
  
def tobase(num, base):
  r = []
  while True:
    r.insert(0, num % base)
    quo = num / base
    num = quo
    if quo == 0:
      break
  return ''.join([str(c) for c in r])
  
def helper(n, b):
  r = str(tobase(n, b))
  prev = []
  while r not in prev:
    prev.append(r)
    r = str(tobase(sum([int(c) ** 2 for c in r]), b))
  return r == '1'

def ishappy(n, b):
  k = (n, b)
  if k not in cache:
    cache[k] = helper(n, b)
  return cache[k]
  
def happygen(b):
  r = 1
  while True:
    r += 1
    while not ishappy(r, b):
      r += 1
    yield r
  
def case(bases):
  gen = happygen(bases[0])
  while True:
    h = gen.next()
    if all([ishappy(h, b) for b in bases]):
      return h
  
def main():
  gen = load('A-small.in')
  n = int(gen.next())
  for i in range(n):
    print 'Case #%d: %d' % (i + 1, case([int(t) for t in gen.next().split()]))

if __name__ == '__main__':
  main()
