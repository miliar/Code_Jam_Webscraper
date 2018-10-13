def solve(plansza):
  zaznaczone = plansza
  n = len(plansza)

  for i, ll in enumerate(plansza):
    for j, l in enumerate(ll):
      if i+1 >= n or j+1 >= n:
        return (False, [])

      if zaznaczone[i][j] == '#':
        zaznaczone[i][j] = '/'
        if zaznaczone[i+1][j] == '#':
          zaznaczone[i+1][j] = '\\'
        else:
          return (False, [])
        
        if zaznaczone[i][j+1] == '#':
          zaznaczone[i][j+1] = '\\'
        else:
          return (False, [])

        if zaznaczone[i+1][j+1] == '#':
          zaznaczone[i+1][j+1] = '/'
        else:
          return (False, [])

  return (True, zaznaczone)



def print_answer(i, ans):
  answer = "Case #{0}:\n".format(1+i)
  if ans[0] == False:
    answer += "Impossible\n"
  else:
    for ll in ans[1]:
      answer += ll + "\n"

  return answer

def solve_file(filename):
  out_name = filename[:-2]+"out"
  ins = open(filename, 'r')
  outs = open(out_name, 'w')

  N = int(ins.readline())

  for i in xrange(N):
    n = map(int, ins.readline())[0]

    test = [ins.readline().strip() for j in range(n)]

    outs.write(print_answer(i, solve(test)))

  ins.close()
  outs.close()



