import sys
input = sys.stdin

T = int(input.readline())

def calc(_L,_H,_others):
  for i in xrange(_L,_H+1):
      for o in _others:
        if i % o == 0 or o % i == 0:
          continue
        else:
          break
      else:
        return i

  return None

for t in xrange(T):
  N,L,H = map(int, input.readline().strip().split(' '))

  others = map(int, input.readline().strip().split(' '))
  ret = calc(L,H,others)

  print 'Case #%d: %s'%(t+1,str(ret) if ret else 'NO')

