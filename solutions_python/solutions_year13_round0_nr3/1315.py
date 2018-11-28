import math

def rf(file):
  return open(file, 'r').readlines()

def pf(fich):
  lines=[f.replace('\n','') for f in rf(fich)]
  n_cases = int(lines[0])
  cases = {}
  for i in range(1, n_cases+1):
    s = lines[i].split(' ')
    a,b = int(s[0]), int(s[1])
    cases[i] = {'a': a, 'b': b}
  return n_cases, cases   
    
def isFairSquare(num):
  p = str(num)
  sqrt = math.sqrt(num)
  if sqrt%1 > 0: return False
  sqrt = str(int(sqrt))
  if p == p[::-1] and sqrt == sqrt[::-1]:
    #print p,
    return True
  return False

def isFairSquare2(num):
  p = str(num)
  if p[-1] != '1' and p[-1] != '2': return False
  sq = num**2
  sq = str(int(sq))
  if p == p[::-1] and sq == sq[::-1]:
    #print p,
    return True
  return False
    
def check(a,b):
  if len(str(b)) > 5:
    max = math.floor(len(str(b))/2.0)
    na = int(10**max)
    na1 = na
    nb1 = int(na*1.2)
    na2 = int(na*2.0)
    nb2 = int(na*2.1)
    step = 1
    rango1 = xrange(na1, nb1+1, step)
    rango2 = xrange(na2, nb2+1, step)
    total = len([c for c in rango1 if isFairSquare2(c)])
    total += len([c for c in rango2 if isFairSquare2(c)])
  else:
    total = len([c for c in xrange(a,b+1) if isFairSquare(c)])
  return total 

def main():
  fich = 'C-small'
  n_cases, cases = pf(fich + '.in')
  f = open(fich + '.o', 'w')
  for n, c in cases.iteritems():
    #print 'Case #%s: %s' % (n, check(c['a'], c['b']))
    f.write('Case #%s: %s\n' % (n, check(c['a'], c['b'])))
  f.close()
   
if __name__ == "__main__":
  main()