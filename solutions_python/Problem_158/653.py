# Richard -> True, Gabriel -> False
D = {
  '111': False,
  '112': False,
  '113': False,
  '114': False,
  '122': False,
  '123': False,
  '124': False,
  '133': False,
  '134': False,
  '144': False,
  '211': True,
  '212': False,
  '213': True,
  '214': False,
  '222': False,
  '223': False,
  '224': False,
  '233': True,
  '234': False,
  '244': False,
  '311': True,
  '312': True,
  '313': True,
  '314': True,
  '322': True,
  '323': False,
  '324': True,
  '333': False,
  '334': False,
  '344': True,
  '411': True,
  '412': True,
  '413': True,
  '414': True,
  '422': True,
  '423': True,
  '424': True,
  '433': True,
  '434': False,
  '444': False
}

filename = 'D-small-attempt0'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
  X, R, C = f.readline().split()

  result = None
  if ((X+R+C in D) and D[X+R+C]) or ((X+C+R in D) and D[X+C+R]):
    result = 'RICHARD'
  else:
    result = 'GABRIEL'

  o.write('Case #%d: %s\n' % (t + 1, result))
