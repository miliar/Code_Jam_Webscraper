


T = input()

def getWP(wins, loses, schedule, i):
  win = wins[i]
  lose = loses[i]

  return win * 1.0 / (win + lose)


def getOWP(wins, loses, schedule, i):
  allP = 0.0
  all = 0

  for j in range(len(wins)):
    if schedule[i][j] == '.': continue

    all += 1

    win = wins[j]
    lose = loses[j]
    if schedule[j][i] == '1': win -= 1
    if schedule[j][i] == '0': lose -= 1

    allP += win * 1.0 / (win + lose)

  return allP / all


for t in range(T):
  print 'Case #{0}:'.format(t+1)

  N = input()
  schedule = []
  for n in range(N):
    schedule.append(raw_input())

  wins = []
  loses = []
  for i in range(N):
    win = 0
    lose = 0
    for j in schedule[i]:
      if j == '1':
        win += 1
      if j == '0':
        lose += 1
    wins.append(win)
    loses.append(lose)


  for i in range(N):
    WP = getWP(wins, loses, schedule, i)
    OWP = getOWP(wins, loses, schedule, i)
    OOWP = 0

    for j in range(N):
      if schedule[i][j] != '.':
        OOWP += getOWP(wins, loses, schedule, j)

    OOWP /= (wins[i] + loses[i])

    print 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

