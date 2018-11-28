import re

PARENS = re.compile(r'[()]')

def load(name):
  f = file(name)
  s = f.readlines()
  f.close()
  return s
  
def repl(m):
  return {'(': '[', ')': ']'}[m.group(0)]
  
def main():
  lines = load('A-large.in')
  l, d, n = [int(t) for t in lines[0].split()]
  words = lines[1: d + 1]
  cases = lines[d + 1: d + n + 1]
  for i, c in enumerate(cases):
    regex = re.compile(PARENS.sub(repl, c))
    print 'Case #%d: %d' % (i + 1, len([w for w in words if regex.match(w)]))

if __name__ == '__main__':
  main()
