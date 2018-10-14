f = open('file.txt')
lnum, j, knum = map(int, f.readline().split())

tmp = f.readlines()
s, c = set(x.strip() for x in tmp[:j]), tuple(x.replace('(', ' *').replace(')', ' ').split() for x in tmp[j:])
del tmp
f.close()

case = tuple()
for l in c:
  tmp = tuple()
  for x in l:
    if x[0] == '*':
      tmp += (x[1:],)
    else:
      tmp += tuple(x)
  case += (tmp,)
del c, tmp

###### Start here #######
for i in xrange(knum):
  v = 0
  for w in s:
    c = 0
    while c<lnum and w[c] in case[i][c]:
      c += 1
    if c == lnum:
      v += 1

  print "Case #%d: %d" % (i+1, v)

