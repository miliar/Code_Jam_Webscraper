import itertools
import math
import numpy
import sys
 
# started at 10:50
# 
 
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
      in_fn = fn
      if out_fn is None:
          out_fn = fn[:-3] + '.out'
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
  # return  list(read_line(f).strip())
  return map(int, list(read_line(f).strip()))
  
def solver(seq):
  # print seq
  i = 0
  while i < len(seq)-1:
    if seq[i] > seq[i+1]:
      #return fix_seq_at(seq, i)
      seq = fix_seq_at(seq, i)
      i = 0
    else:
      i+=1
  return int(''.join(map(str,seq)))

def fix_seq_at(seq, at):
  res = list(seq)
  res[at] -= 1
  i = at + 1
  while i < len(seq):
    res[i] = 9
    i+=1
  #return ''.join(map(str,res))
  return res
################################################################################ 
 
# 111111111111111110
# 111111111111111109
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