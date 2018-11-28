import sys

fin = open('al0.in', 'r')
fout = open('a.out', 'w')

ncases = int(fin.readline())
for tc in xrange(0, ncases):
  n = int(fin.readline())
  s = []
  for j in xrange(0, n):
    s.append(fin.readline())
  wp = []
  ng = []
  nw = []
  for i in xrange(0, n):
    ngames = 0
    nwins = 0
    for j in xrange(0, n):
      if s[i][j] == "1":
        nwins += 1
      if s[i][j] != ".":
        ngames += 1
    wp.append(float(nwins) / ngames)
    ng.append(ngames)
    nw.append(nwins)

  owp = []
  for i in xrange(0, n):
    acu = 0
    for j in xrange(0, n):
      if s[i][j] != '.':
        acu += float(nw[j] - (1 if s[j][i] == "1" else 0)) / (ng[j] - (0 if s[j][i] == "." else 1))
    owp.append(acu / ng[i])

  oowp = []
  for i in xrange(0, n):
    acu = 0
    for j in xrange(0, n):
      if s[i][j] != '.':
        acu += owp[j]
    oowp.append(acu / ng[i])

  fout.write("Case #" + str(tc + 1) + ":\n")
  for i in xrange(0, n):
    fout.write(str(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) + "\n")
