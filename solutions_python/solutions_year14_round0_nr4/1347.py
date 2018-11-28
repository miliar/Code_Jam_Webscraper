def r_f():
  return map(float, raw_input().split())
def r_i():
  return map(int, raw_input().split())

def play_1(a):
  return a[-1]

def play_2(a, chosenNaomi):
  for p in a:
    if p >= chosenNaomi:
      return p
  return a[0]


def play_1d(a1, a2):
  if a1[0] < a2[0]:
    return (a1[0], a2[-1])
  return (a1[-1])

def solve_dwar(n, a1, a2):
  naomi = 0
  for k in range(0, n):
    (chosenNaomi, toldNaomi) = play_1d(a1, a2)
    chosenKen = play_2(a2, toldNaomi)
    if chosenNaomi > chosenKen:
      naomi += 1
    a1.remove(chosenNaomi)
    a2.remove(chosenKen)
  return naomi


def solve_dwar2(n, a1, a2):
  naomi = 0
  i, j = n - 1, n - 1
  while i >= 0:
    if a1[j] > a2[i]:
      naomi += 1
      j -= 1
    i -= 1
  return naomi


def solve_war(n, a1, a2):
  naomi = 0
  for k in range(0, n):
    chosenNaomi = play_1(a1)
    chosenKen = play_2(a2, chosenNaomi)
    if chosenNaomi > chosenKen:
      naomi += 1
    a1.remove(chosenNaomi)
    a2.remove(chosenKen)
  return naomi

def solve(n, a1, a2):
  a1 = sorted(a1)
  a2 = sorted(a2)
  return "%s %s" % (solve_dwar2(n, a1[:], a2[:]), solve_war(n, a1[:], a2[:]))



(t,) = r_i()
for i in range(1, t + 1):
  ((n,), a1, a2) = (r_i(), r_f(), r_f())
  print "Case #%s: %s" % (i, solve(n, a1, a2))
