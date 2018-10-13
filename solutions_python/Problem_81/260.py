from fractions import Fraction

for case in range(1, int(input()) + 1):
  N = int(input())
  teams = [input() for _ in range(N)]

  ws = [t.count('1') for t in teams]
  gs = [len(t) - t.count('.') for t in teams]

  wp = [Fraction(ws[i], gs[i]) for i in range(N)]

  owp = []
  for i, t in enumerate(teams):
    p = 0
    for j, o in enumerate(t):
      if o == '.':
        continue
      p += Fraction(ws[j] - int(t[j] == '0'), gs[j] - 1)
    owp.append(p / gs[i])

  oowp = []
  for i, t in enumerate(teams):
    oowp.append(sum(owp[j] for j in range(N) if t[j] != '.') / gs[i])

  print('Case #%d:' % case)
  for n in range(N):
    print(.25 * wp[n] + .5 * owp[n] + .25 * oowp[n])
