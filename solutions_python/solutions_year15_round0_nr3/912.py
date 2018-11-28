from itertools import izip

def main():
  t = int(raw_input())
  for i in xrange(t):
    l, x = map(int, raw_input().split())
    chars = raw_input()
    r = can_reduce(chars, x)
    if r:
      name = 'YES'
    else:
      name = 'NO'
    print "Case #%d: %s"%(i+1, name)

char2int = {}
char2int['1'] = 1
char2int['i'] = 2
char2int['j'] = 3
char2int['k'] = 4
char2int['-1'] = -1
char2int['-i'] = -2
char2int['-j'] = -3
char2int['-k'] = -4

int2char = {v: k for k, v in char2int.items()}

mat = [[1, 2, 3, 4],
       [2,-1, 4,-3],
       [3,-4,-1, 2],
       [4, 3,-2,-1]]

def sign(a):
  if a > 0:
    return 1
  else:
    return -1

def abs(a):
  if a < 0:
    return -a
  else:
    return a

def mult(a, b):
  return sign(a*b)*mat[abs(a)-1][abs(b)-1]

def get_mtable():
  mtable = {}
  for i in xrange(-4, 5):
    if i != 0:
      for j in xrange(-4, 5):
        if j != 0:
          mtable[(i,j)] = mult(i,j)
  return mtable
mtable = get_mtable()

def get_dtable():
  dtable = {(i,v): j for (i,j), v in mtable.items()}
  return dtable
dtable = get_dtable()

def pmult(a, b):
  r = mult(char2int[a], char2int[b])
  return int2char[r]

def test_pmult():
  for i in char2int.keys():
    for j in char2int.keys():
      print "%s*%s = %s"%(i,j,pmult(i,j))

def can_reduce(chars, x):
  chars = x*chars
  seq = [char2int[c] for c in chars]
  if mult_all(seq) != -1:
    return False
  return can_reduce0(seq, 0, [2,3,4])

def mult_all(seq):
  seq = seq[:]
  n = len(seq)
  if n == 1:
    return seq[0]
  iter_seq = seq[:]
  iter_n = len(iter_seq)
  new_seq = seq
  new_n = iter_n/2
  while iter_n > 1:
    for i, (v1,v2) in enumerate(izip(iter_seq[:iter_n:2],iter_seq[1:iter_n:2])):
      new_seq[i] = mtable[v1,v2]
    if iter_n%2 != 0:
      new_seq[new_n-1] = mtable[new_seq[new_n-1], iter_seq[iter_n-1]]
    new_seq, iter_seq = iter_seq, new_seq
    new_n, iter_n = new_n/2, new_n
  return iter_seq[0]

def test_mult_all(seq):
  print mult_all(seq)
  print reduce(lambda x,y: mtable[x,y], seq)

def can_reduce0(seq, s, target):
  if len(target) == 1:
    return True
  if len(seq) == s:
    return False
  t0 = target[0]
  target1 = target[1:]
  acc = 1
  for i in xrange(s, len(seq)):
    e = seq[i]
    acc = mtable[acc, e]
    if t0 == acc:
      r = can_reduce0(seq, i+1, target1)
      if r:
        return r
  return False

main()
