import sys

conv = {'.': 7, 'X': 1, 'O': 2, 'T': 0} # bitwise 111 , 001, 010, 000
rconv = {v:k for k, v in conv.items()}

def print_dset(d):
  for i in range(4):
    for j in range(4):
      print d[i][j],
    print

def input(filename):
  f = open(filename)
  num = int(f.readline().strip())
  for i in range(num):
    dset = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(4):
      line = f.readline().strip()
      for k in range(4):
        dset[j][k] = conv[line[k]]
    # empty line:
    f.readline()
    #print_dset(dset)
    yield dset

def do_work(dset):
  # rows:
  total = 0
  for i in range(4):
    res = 0
    for j in range(4):
      res |= dset[i][j]
    if res in (1, 2):
      return '%s won' % rconv[res]
    total |= res
  # cols:
  for j in range(4):
    res = 0
    for i in range(4):
      res |= dset[i][j]
    if res in (1, 2):
      return '%s won' % rconv[res]
    total |= res
  # diag 1:
  res = 0
  for i in range(4):
    res |= dset[i][i]
  if res in (1, 2):
    return '%s won' % rconv[res]
  total |= res
  # diag 2:
  res = 0
  for i in range(4):
    res |= dset[i][3 - i]
  if res in (1, 2):
    return '%s won' % rconv[res]
  total |= res

  if total == 7:
    return 'Game has not completed'
  else:
    return 'Draw'


if __name__ == '__main__':
  gen = input(sys.argv[1])
  for i, dset in enumerate(gen):
    print 'Case #%s: %s' % (i+1, do_work(dset))
