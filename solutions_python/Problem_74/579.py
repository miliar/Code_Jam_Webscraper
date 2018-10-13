input = [line[:-1] for line in file("in")][1:]

case = 0
for line in input:
  case += 1

  line = line.split(" ")[1:]
  line = zip(line[::2], line[1::2])

  time = {'O' : 0, 'B' : 0}
  position = {'O' : 1, 'B' : 1}

  other = {'O' : 'B', 'B' : 'O'}

  for order in line:
    robot = order[0]
    pos = int(order[1])

    time[robot] = max(time[other[robot]], time[robot] + abs(pos - position[robot])) + 1
    position[robot] = pos

  print "Case #%d: %d" % (case, max(time['O'], time['B']))
