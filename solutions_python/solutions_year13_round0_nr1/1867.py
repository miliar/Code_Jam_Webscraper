f = open('Al')

def message(sum):
  if sum == 164 or sum == 168:
    return 'X won'
  elif sum == 132 or sum == 137:
    return 'O won'
  else:
    return None

num_cases = int(f.next())
for T in range(1,num_cases+1):
  mtx = [[],[],[],[],[],[],[],[],[],[]]
  full = True
  for i in range(0, 4):
    line = list(f.next().strip())
    if '.' in line:
      full = False
    vals = map(lambda x: ord(x) - 46, line)
    mtx[i] = vals
    for j in range(4, 8):
      mtx[j].append(vals[j-4])

    mtx[8].append(vals[i])
    mtx[9].append(vals[3-i])

  msgs = filter(lambda x: not x is None, map(message, map(sum, mtx)))
  msg = ''

  if len(msgs) == 0:
    if full:
      msg = 'Draw'
    else:
      msg = 'Game has not completed'
  else:
    msg = msgs[0]

  print "Case #%s: %s" % (T, msg)
  if T < num_cases:
    f.next()
