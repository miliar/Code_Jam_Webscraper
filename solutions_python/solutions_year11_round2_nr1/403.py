#!/usr/bin/python

num_cases = int(raw_input())

# TODO remember edge case of 2 combs with equal profit

for i in range(0, num_cases):
  print("Case #%d:" % (i + 1))
  n     = int(raw_input())
  score = []

  for j in range(0, n):
    line = raw_input()
    score_line = []
    for k in range(0, len(line)):
      current = line[k]
      if current == '.':
        score_line.append(-1)
      else:
        score_line.append(int(current))
    score.append(score_line)
 
  table = [[float(0)]*n for x in xrange(n)]
  wps  = []

  for j in range(0, n):
    total = 0
    wins  = 0
    for k in range(0, n):
      current = score[j][k]
      if current >= 0:
        total += 1
        wins += current
    if total > 0:
      wps.append(float(wins)/float(total))
    else:
      wps.append(float(0))

    for k in range(0, n):
      current = score[j][k]
      if current >= 0:
        temp_wins = wins
        temp_total = total - 1
        if current == 1:
          temp_wins -= 1
        if temp_total > 0:
          table[j][k] = float(temp_wins)/float(temp_total)
        else:
          table[j][k] = float(0)
      else:
        table[j][k] = float(0)
  owps = []
  for j in range(0, n):
    owp = float(0)
    total = 0
    for k in range(0, n):
      current = score[j][k]
      if current >= 0:
        owp += table[k][j]
        total += 1
    if total > 0:
      owp /= total
    owps.append(owp)

  for j in range(0, n):
    oowp = float(0)
    total = 0
    for k in range(0, n):
      current = score[j][k]
      if current >= 0:
        oowp += owps[k]
        total += 1
    if total > 0:
      oowp /= total
    rpi = (0.25 * wps[j]) + (0.50 * owps[j]) + (0.25 * oowp)
    print(rpi)


