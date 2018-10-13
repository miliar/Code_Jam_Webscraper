text = 'welcome to code jam'

def load(name):
  f = file(name)
  s = f.readlines()
  f.close()
  return s
  
def howmany(this, that):
  lthis = len(this)
  lthat = len(that)
  if lthis > lthat:
    r = 0
  elif lthis == 1:
    r = that.count(this)
  else:
    r = 0
    rest = that
    n = that.count(this[0])
    for i in range(n):
      rest = rest[rest.find(this[0]) + 1:]
      r += howmany(this[1:], rest)
  return r
  
def case(data):
  return howmany(text, data)
  
def main():
  lines = load('C-small.in')
  n = int(lines[0])
  for i in range(n):
    r = str(case(lines[i + 1].strip()))
    print 'Case #%d: %s' % (i + 1, len(r) < 4 and '%04d' % (int(r)) or r[-4: -1])

if __name__ == '__main__':
  main()
