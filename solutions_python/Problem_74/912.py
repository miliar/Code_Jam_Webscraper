def ints():
  return map(int, raw_input().split())

def items():
  return raw_input().split()

num_cases, = ints()

for case_num in xrange(1, num_cases + 1):
  tmp = items()
  N, sequence = int(tmp[0]), tmp[1:]
  x, time, O, B, Ot, Bt = 0, 0, 1, 1, 0, 0
  while x < N:
    tic, xtic = 0, 0
    for i in xrange(x*2, N*2, 2):
      if (sequence[i] == 'O') & (Ot == 0):
        Ot = int(sequence[i+1])
      elif (sequence[i] == 'B') & (Bt == 0):
        Bt = int(sequence[i+1])
    
    if O == Ot:
      if sequence[x*2] == 'O':
        xtic = 1
        Ot = 0
        tic = 1
    else:
      O += abs(Ot-O)/(Ot-O)
      tic = 1

    if B == Bt:
      if sequence[x*2] == 'B':
        xtic += 1
        Bt = 0
        tic = 1
    else:
      B += abs(Bt-B)/(Bt-B)
      tic = 1

    time += tic
    x += xtic

  print "Case #%d: %d" % (case_num, time)
