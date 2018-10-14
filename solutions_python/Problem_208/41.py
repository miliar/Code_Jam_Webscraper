import os
import math

def solve(N, horses, cities, start, end):
  dp = {}
  visited = {}
  for i in range(N):
    visited[i] = {}
    dp[i] = {}
  dp[start] = {
    start: (horses[start][0], 0)
  }

  while True:
    mintime = -1
    use_city = -1
    use_horse = -1
    for icity, horse_m in dp.iteritems():
      for ihorse, (endur, time) in horse_m.iteritems():
        if ihorse in visited[icity]:
          continue
        if time > mintime and mintime >=0:
          continue
        mintime = time
        use_city = icity
        use_horse = ihorse
    if use_city == end:
      return mintime

    visited[use_city][use_horse] = True

    # Use current horse
    # (speed, endur)
    current_horse = use_horse
    speed = horses[use_horse][1]
    endur = dp[use_city][use_horse][0]
    for next_city, dis in enumerate(cities[use_city]):
      if dis < 0:
        continue
      if endur < dis:
        continue
      if current_horse in visited[next_city]:
        continue
      next_time = mintime + float(dis) / speed
      next_endur = endur - dis
      if current_horse in dp[next_city] and dp[next_city][current_horse][1] < next_time:
        continue
      dp[next_city][current_horse] = (next_endur, next_time)

    # Use city horse
    # (speed, endur)
    current_horse = use_city
    speed = horses[use_city][1]
    endur = horses[use_city][0]
    for next_city, dis in enumerate(cities[use_city]):
      if dis < 0:
        continue
      if endur < dis:
        continue
      if current_horse in visited[next_city]:
        continue
      next_time = mintime + float(dis) / speed
      next_endur = endur - dis
      if current_horse in dp[next_city] and dp[next_city][current_horse][1] < next_time:
        continue
      dp[next_city][current_horse] = (next_endur, next_time)


fin = open('C-large (1).in', 'r')
fout = open('C.out', 'w')
nown = 0
nowt = 0
t = int(fin.readline())
for nowt in range(t):
  nowt += 1
  line = fin.readline()
  N, Q = line.split()
  N = int(N)
  Q = int(Q)
  horses = []
  cities = []
  for i in range(N):
    line = fin.readline()
    dis, speed = line.split()
    dis = int(dis)
    speed = int(speed)
    horses.append((dis, speed))
  for i in range(N):
    line = fin.readline()
    parts = [int(part) for part in line.split()]
    cities.append(parts)
  results = []
  for i in range(Q):
    line = fin.readline()
    start, end = line.split()
    start = int(start) - 1
    end = int(end) - 1
    results.append(solve(N, horses, cities, start, end))

  out_str = 'Case #%d: %s\n' % (nowt, " ".join(["{0:.15f}".format(r) for r in results]))
  print out_str
  fout.write(out_str)
fin.close()
fout.close()
