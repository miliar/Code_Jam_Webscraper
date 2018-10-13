import sys

def IN():
  return sys.stdin.readline()

def OUT(txt):
  ERR("[OUT] " + txt)
  sys.stdout.write(txt)
  sys.stdout.flush()

def ERR(txt):
  print >> sys.stderr, txt

ERR("start")

def do_case(num):
  OUT("Case #" + str(num + 1) + ": ")
  board = [x[:-1] for x in (IN() for _ in range(4))]
  IN()
  ERR(board)
  check = ([tuple((x, y) for y in range(4)) for x in range(4)] +
           [tuple((x, y) for x in range(4)) for y in range(4)] +
           [tuple((i, f(i)) for i in range(4)) for f in (lambda x: x, lambda x: 3 - x)])
  empty_present = False
  for cur in check:
    vals = tuple(board[x][y] for x, y in cur)
    if all(v in {'X', 'T'} for v in vals):
      OUT("X won\n")
      return
    elif all(v in {'O', 'T'} for v in vals):
      OUT("O won\n")
      return
    elif any(v == '.' for v in vals):
      empty_present = True
  if empty_present:
    OUT("Game has not completed\n")
  else:
    OUT("Draw\n")

for case in range(int(IN())):
  do_case(case)

sys.stdout.flush()
