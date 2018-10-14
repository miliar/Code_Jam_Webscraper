def gen_teams(rnd, game):
  n = 2**(rnd+1)
  start = game*n
  for team in xrange(start, start+n):
    yield team

#import sys
#for i in gen_teams(2, 1):
#  print >> sys.stderr, i

def can_miss(M, rnd, game):
  for team in gen_teams(rnd, game):
    if M[team] <= 0:
      return False
  return True

def miss(M, rnd, game):
  for team in gen_teams(rnd, game):
    M[team] -= 1

for case in xrange(1, int(raw_input())+1):
  P = int(raw_input())
  M = map(int, raw_input().split())
  games = []
  for rnd in xrange(P):
    for i, c in enumerate(map(int, raw_input().split())):
      games.append((c, -rnd, -i))
  games.sort(reverse=True)

  total = 0
  for i, g in enumerate(games):
    if can_miss(M, -g[1], -g[2]):
      miss(M, -g[1], -g[2])
    else:
      total += g[0]

  print "Case #%d: %d" % (case, total)
