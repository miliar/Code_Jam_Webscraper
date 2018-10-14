def solve(plansza):
  print plansza,
  n = len(plansza)
  wins = [0 for i in plansza]
  totals = [0 for i in plansza]

  ows = [0 for i in plansza]
  oows = [0 for i in plansza]


  for i, ll in enumerate(plansza):
    for j, wyn in enumerate(ll):
      if wyn == '0':
        totals[i] += 1.0
      elif wyn == '1':
        totals[i] += 1.0
        wins[i] += 1.0


  for i, ll in enumerate(plansza):
    my = 0.0
    m = 0.0
    for j, wyn in enumerate(ll):
      if i != j:
        if wyn == '1':          # Moze na odwrot 
          my += (wins[j]) / (totals[j] - 1)
          m += 1.0
        elif wyn == '0':
          my += (wins[j] - 1.0) / (totals[j] - 1)
          m += 1.0
        # else:
        #   my += wins[j] / totals[j]



    ows[i] = my / m


  for i, ll in enumerate(plansza):
    my = 0.0
    m = 0.0
    for j, wyn in enumerate(ll):
      if wyn != '.':
        m += 1.0
        my += ows[j]

    oows[i] = my / m


  wp = [(wins[i] / totals[i]) for i in range(n)]

  print wp
  print ows
  print oows


  res = [0.25 * wp[i] + 0.5 * ows[i] + 0.25 * oows[i] for i in range(n)]

  return res



def print_answer(i, ans):
  answer = "Case #{0}:\n".format(1+i)
  for a in ans:
    answer += a

  return answer

def solve_file(filename):
  out_name = filename[:-2]+"out"
  ins = open(filename, 'r')
  outs = open(out_name, 'w')

  N = int(ins.readline())

  for i in xrange(N):
    n = int(ins.readline())

    test = [ins.readline().strip() for j in range(n)]

    outs.write(print_answer(i, solve(test)))

  ins.close()
  outs.close()



