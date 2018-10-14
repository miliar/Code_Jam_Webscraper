for tc in range(input()):
  n, r, o, y, g, b, v = raw_input().split()
  n, r, o, y, g, b, v = int(n), int(r), int(o), int(y), int(g), int(b), int(v)
  if r > n/2 or y > n/2 or b > n/2:
    answer = "IMPOSSIBLE"
  else:
    to_place = {'R': r, 'Y': y, 'B': b}
    for j in to_place:
      if to_place[j] == max(to_place.values()):
        answer = j
        to_place[j] += -1
        break
    for i in range(n - 1):
      if answer[-1] == 'R':
        if to_place['Y'] >= to_place['B']:
          answer += 'Y'
          to_place['Y'] += -1
        else:
          answer += 'B'
          to_place['B'] += -1
      elif answer[-1] == 'B':
        if to_place['Y'] >= to_place['R']:
          answer += 'Y'
          to_place['Y'] += -1
        else:
          answer += 'R'
          to_place['R'] += -1
      elif answer[-1] == 'Y':
        if to_place['R'] >= to_place['B']:
          answer += 'R'
          to_place['R'] += -1
        else:
          answer += 'B'
          to_place['B'] += -1
  if answer[0] == 'B' and answer[-2] + answer[-1] == 'RB':
    answer = answer[0:len(answer)-2] + 'BR'
  print "Case #" + str(tc+1) + ": " + answer