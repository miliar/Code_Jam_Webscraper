from __future__ import print_function
CASES = int(raw_input())

for I in range(CASES):
  inp = raw_input().split()[1:]
  inp = zip(inp[::2], [int(x) for x in inp[1::2]])
  
  Oevents = []
  Bevents = []
  for i, (b, t) in enumerate(inp):
    if b == 'B': Bevents.append((t, i))
    if b == 'O': Oevents.append((t, i))

  #print(Oevents, Bevents)

  Q = []
  O = 'O'
  B = 'B'

  o_arrival = -1
  b_arrival = -1
  last_n = -1
  RET = 0

  if Oevents:
    Q.append(Oevents[0][0])
    o_arrival = Oevents[0][0]

  if Bevents:
    Q.append(Bevents[0][0])
    b_arrival = Bevents[0][0]

  while Q:
    Q = list(set(Q))
    Q.sort()
    #print(('o%d b%d last_n=%d' % (o_arrival, b_arrival, last_n)).ljust(18), repr(Q).ljust(14), repr(Oevents).ljust(18), Bevents)
    t = Q.pop(0)

    if Oevents and t >= o_arrival and Oevents[0][1] == last_n+1:
      RET = t
      last_n +=1
      last = Oevents[0]
      Q.append(t+1)
      del Oevents[0]
      if Oevents:
        o_arrival = t+1+abs(last[0] - Oevents[0][0])
        Q.append(o_arrival)
      continue

    if Bevents and t >= b_arrival and Bevents[0][1] == last_n+1:
      RET = t
      last_n +=1
      last = Bevents[0]
      Q.append(t+1)
      del Bevents[0]
      if Bevents:
        b_arrival = t+1+abs(last[0] - Bevents[0][0])
        Q.append(b_arrival)
      continue

  print('Case #%d:'%(I+1), RET)
  
