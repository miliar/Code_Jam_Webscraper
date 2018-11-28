def rf(file):
  return open(file, 'r').readlines()

def pf(fich):
  lines=[f.replace('\n','') for f in rf(fich)]
  n_cases = int(lines[0])
  cases = {}
  for i in range(1, n_cases+1):
    j = 1 if i == 1 else j+5
    cases[i] = [list(l) for l in lines[j:i*5]]
  return n_cases, cases   
    
def check(m):
  #filas
  for f in m:
    if ((f.count('X') == 3 and 'T' in f) or f.count('X') == 4):
      return 'X won'
    
    if ((f.count('O') == 3 and 'T' in f) or f.count('O') == 4):
      return 'O won'
    
  #cols
  cols = zip(m[0], m[1], m[2], m[3])
  for c in cols:
    if ((c.count('X') == 3 and 'T' in c) or c.count('X') == 4):
      return 'X won'
    
    if ((c.count('O') == 3 and 'T' in c) or c.count('O') == 4):
      return 'O won'
  
  # diagonal
  diag = [[m[0][0], m[1][1], m[2][2], m[3][3]],
          [m[0][3], m[1][2], m[2][1], m[3][0]]]
  for d in diag:
    if ((d.count('X') == 3 and 'T' in d) or d.count('X') == 4):
      return 'X won'
    
    if ((d.count('O') == 3 and 'T' in d) or d.count('O') == 4):
      return 'O won'
    
  # vacio
  if '.' not in [c for f in m for c in f]:
    return 'Draw'
  
  return 'Game has not completed'
    
def main():
  n_cases, cases = pf('A-large.in')
  f = open('A-large.o', 'w')
  for n, m in cases.iteritems():
    print 'Case #%s: %s' % (n, check(m))
    f.write('Case #%s: %s\n' % (n, check(m)))
  f.close()
      
if __name__ == "__main__":
  main()