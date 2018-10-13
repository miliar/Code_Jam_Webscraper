import itertools
import math
import numpy
import sys

#started at 11:15

def read_line(f):
  return next(f)

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res

def solve(solver, fn=None, out_fn=None):
    if fn is None:
      fi = sys.stdin
      fo = sys.stdout
      process_cases(fi,fo,solver)
    else:
      in_fn = fn + '.in'
      if out_fn is None:
          out_fn = fn + '.out'
      with open(in_fn, 'r') as fi:
          with open(out_fn, 'w') as fo:
            process_cases(fi,fo,solver)
            
def process_cases(fi, fo, solver):
  T = read_int(fi)
  for i in range(T):
      case = read_case(fi)
      res = solver(case)
      write_case(fo, i+1, res)
    
################################################################################

def write_case(f, i, res):
  f.write('Case #%d: '%i)
  f.write('%s'%res)
  f.write('\n')

def read_case(f):
  #n = read_int(f)
  #m = read_int(f)
  n,m = read_ints(f)
  g = []
  for i in xrange(n):
    g.append(read_ints(f))
  return (n,m,g)
def solver(case):
  n,m,g = case
  
  minimum = find_minimum(g)
  while(minimum != 0):
    decrement_by(g, minimum)
    zeros = find_zeros(g)
    r  = validate_zeros(g, zeros)
    if r == False:
      return "NO"
    minimum = find_minimum(g)
  return "YES"

def validate_zeros(g, zeros):
  for z in zeros:
    #all columns are 0
    if sum(g[z[0]]) == 0:
      continue
    
    #all row in this column are 0
    for i in xrange(len(g)):
      if g[i][z[1]] != 0:
        return False
  return True

def find_zeros(g):
  res_v = {i : {} for i in range(len(g))}
  res_h = {i : {} for i in range(len(g[0]))}
  zeros = []
  r = 0
  for row in g:
    c = 0
    for col in row:
      if col == 0:
        zeros.append( (r,c) )
      c += 1
    r += 1
  return zeros
def decrement_by(g, val):
  r = 0
  for row in g:
    c = 0
    for col in row:
      g[r][c] -= val
      c += 1
    r += 1

def find_minimum(g):
  r = min(g[0])
  for row in g[1:]:
    r = min(r, min(row))
  return r  

def old():
  
  constraints = []
  for i in xrange(n):
    for j in xrange(m):
      h = g[i][j]
      constraints.append([('row', i, h), ('col', j, h) ])
  
  
################################################################################ 

 
def main():
  method = solver
  if(len(sys.argv) == 2):
    solve(method, sys.argv[1])
  elif len(sys.argv) == 3:
    solve(method, sys.argv[1], sys.argv[2])
  else:
    solve(method)

def debug(*args, **kwargs):
  if False:
    s = ' '.join(map(str, args))
    if len(kwargs) == 0:
      print(s)
    else:
      for k,v in kwargs.iteritems():
        print s, k,'=',v

if __name__ == "__main__":
  main()