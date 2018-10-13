from itertools import *
from pprint import pprint

mat = {
  'jk': [1, 'i'],
  'kj': [-1, 'i'],
  'ik': [-1, 'j'],
  'ki': [1, 'j'],
  'ij': [1, 'k'],
  'ji': [-1, 'k'],

  'ii': [-1, '1'],
  'jj': [-1, '1'],
  'kk': [-1, '1'],

  '1i': [1, 'i'],
  '1j': [1, 'j'],
  '1k': [1, 'k'],  
}

def mul(a, b):
  # print 'mul', a, b
  ans = mat[a[1] + b[1]][:]
  # print a[1] + b[1], ans, ans[0], a[0], b[0]
  ans[0] = ans[0] * a[0] * b[0]
  return ans

def solve(fi, fo, ti):
  _lx = fi.readline().strip().split(' ')
  l, x = int(_lx[0]), int(_lx[1])
  lx = fi.readline().strip()

  if x == 1 and lx == 'ijk':
    return 'YES'

  if l < 3 and ( (l * x) < 3 ):
    return 'NO'

  if len(set(lx)) == 1:
    return 'NO'


  floop = False  
  total = l * x
  possible = False
  matched = {'i':-1, 'j':-1, 'k':-1}

  
  m = [1, lx[0]]
  for i in xrange(1, total):
    # print m, [1, lx[i%l]]
    if (matched['i'] == -1) and (m[0] == 1) and (m[1] == 'i'):
      matched['i'] = i - 1

    m = mul(m, [1, lx[i%l]])

  if m and m[0] == -1 and m[1] == '1':
    floop = True

  # print m, i

  if floop and (matched['i'] > -1):
    looks = ['i', 'j', 'k']
    _lookup_index = 1
    _index = _start_index = matched['i'] + 1
    # print 'I', (lx * x)[0:matched['i']+1]
    m = [1, lx[_start_index%l]]

    while _lookup_index < 3:

      if (_index == total):
        _start_index += 1
        if _start_index == total:
          break

        _index = _start_index
        _lookup_index = 0
        m = [1, lx[_start_index%l]]

      _c = looks[_lookup_index]
      _index += 1

      # print m, [1, lx[_index%l]]
      m = mul(m, [1, lx[_index%l]])

      if (m[0] == 1) and (m[1] == _c):
        if _lookup_index == 2 and _index != (total-1):
          continue

        matched[_c] = _index
        _index += 1
        m = [1, lx[(_index)%l]]
        _lookup_index += 1

        # if _c == 'j':
        #   print 'J', (lx * x)[matched['i']+1:matched['j']+1]
        # if _c == 'k':
        #   print 'K', (lx * x)[matched['j']+1:matched['k']]          

    if _lookup_index == 3:
      # return 'YES, %s' % matched
      return 'YES'
      

  return 'NO'

  
  # m = [1, lx[0]]
  # for i in range(1, len(lx)):
  #   # print m, [1, lx[i]]
  #   m = mul(m, [1, lx[i]])

  # # print m
  # if m and m[0] == -1 and (x % 4) == 0:
  #   possible = True

  # elif m and m[0] == 1 and (x-2 % 4) == 0 and x > 2:
  #   possible = True

  # elif m and m[0] == -1 and m[1] == '1':
  #   possible = True

  # if (floop == False) and (possible == True):
  #   print '='*50
  #   print lx, x, floop, possible
  #   # df
  # return '%s,%s' % (floop, possible)

def main(f):
  fi = open(f + '.in')
  fo = open(f + '.out', 'w')

  T = int(fi.readline())
  for ti in range(T):
    #fi.readline().strip()
    # print 'C', ti+1
    out = solve(fi, fo, ti)
    fo.write("Case #%d: %s\n" % ((ti+1), out) )
    print "Case #%d: %s" %  ((ti+1), out) 

if __name__ == "__main__":
  main('C-small-attempt2')
  # main('sample')

