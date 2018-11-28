import sys

inputFile = sys.stdin
count = int(inputFile.readline())

def add(dirs, new) :
  # print dirs, new
  cur = dirs['/']
  count = 0
  for piece in new:
    if piece == '': continue
    if not cur.has_key(piece):
      count += 1
      cur[piece] = {}

    cur = cur[piece]
  return (dirs, count)

for lineno in xrange(1, count+1):
  N, M = map(int, inputFile.readline().split())

  exist = {'/':{}}
  for n in xrange(N):
    exist, count = add(exist, inputFile.readline().strip().split('/')[1:])

  num = 0
  
  for m in xrange(M):
    exist, count = add(exist, inputFile.readline().strip().split('/')[1:])
    num += count
  
  print "Case #%d:" % lineno, 
  print num
  sys.stdout.flush()

  lineno += 1
