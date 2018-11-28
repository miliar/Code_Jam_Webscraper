T = int(raw_input())

for tt in range(T):
  cost = 0
  N, M = map(int, raw_input().split())
  enter = {}
  exit = {}
  for i in range(M):
    a, b, c = map(int, raw_input().split())
    d = b-a+1
    cost += (d*d + d - 2) / 2 * c
    if not a in enter:
      enter[a] = 0
    enter[a] += c
    if not b in exit:
      exit[b] = 0
    exit[b] += c
  
  exits = exit.keys()
  exits.sort()
  cur_exit = len(exits) - 1
  
  entrances = enter.keys()
  entrances.sort()
  entrances.reverse()
  
  acost = 0
  for key in entrances:
    while cur_exit > 0 and exits[cur_exit-1] >= key:
      cur_exit -= 1
    use_exit = cur_exit
    while enter[key] > 0:
      x = exits[use_exit]
      use = min(exit[x], enter[key])
      d = x - key + 1
      acost += (d*d + d - 2) / 2 * use
      enter[key] -= use
      exit[x] -= use
      use_exit += 1
  print "Case #%d: %d" % (tt+1, acost - cost)