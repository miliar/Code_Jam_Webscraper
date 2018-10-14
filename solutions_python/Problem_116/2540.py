import itertools
import math
import numpy
import sys

#started at 9:13

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
  m = []
  for i in xrange(4):
    m.append(read_letters(f))
  try:
    read_line(f)
  except:
    pass
  return m
  
def solver(m):
  for l in m:
    debug( ''.join(l))
      
  s = []
  for i in xrange(4):
    s.append([])
    for j in xrange(4):
      piece = m[i][j]
      values = {'up':1, 'left':1, 'diag':1, 'invd':1} #, 'i':i, 'j':j
      debug(i,j, piece = piece)
      for n in get_neighbours(i,j):
        n_piece = m[n[0]][n[1]]
        n_values = s[n[0]][n[1]]
        direction = n[2]
        #debug("  neighbour",n, "with piece", n_piece)
        #debug("    values:", **n_values) 
        if same_team(piece, n_piece):
          if n_piece != "T":
            values[direction] = n_values[direction] +1
          else:
            t_side = find_side(m, n[0], n[1], direction)
            if same_team(piece, t_side):
              values[direction] = n_values[direction] +1
            else:
              values[direction] = 2
          if values[direction] == 4:
            side = find_side(m, i, j, direction)
            return side+" won"
        else:
          values[direction] = 1
      s[i].append(values) 
      debug("  self values:", **values)
  for l in m:
    if '.' in l:
      return "Game has not completed"
  return "Draw"
def find_side(m, i,j, direction):
  try:
    while(True):
      if m[i][j] == 'X' or m[i][j] == 'O':
        return m[i][j]
      if direction == 'up':
        i-=1
      elif direction == 'left':
        j-=1
      elif direction == 'diag':
        i -= 1
        j -= 1
      elif direction == 'invd':
        i -= 1
        j += 1
  except:
    return None
def same_team(a,b):
  if a == "." and b == ".":
    return False
  return a == b or  a == "T" or b == "T"

def get_neighbours(i,j):
  if i > 0:
    yield (i-1, j, 'up')
  if j > 0:
    yield (i, j-1, 'left')
  if i > 0 and j > 0:
    yield (i-1, j-1, 'diag')
  if i > 0 and j < 3:
    yield (i-1, j+1, 'invd')
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