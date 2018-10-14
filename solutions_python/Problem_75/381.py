import re
from string import uppercase

def make_coms(coms):
  coms = coms.split()
  com_dict = {}

  for u in uppercase:
    com_dict[u] = {}
    com_dict[u].setdefault(-1)
  
  for c in coms:
    c0 = c[0]
    c1 = c[1]
    c2 = c[2]

    com_dict[c0][c1] = c2
    com_dict[c1][c0] = c2

  return com_dict

def make_opps(opps):
  opps = opps.split()
  opp_dict = {}

  for u in uppercase:
    opp_dict[u] = set()

  for o in opps:
    opp_dict[o[0]].add(o[1])
    opp_dict[o[1]].add( o[0])

  return opp_dict
    
def parse(line):
  inputs = re.split('[0-9]*', line)
  invs = inputs[-1].strip()
  opps = inputs[-2]
  coms = inputs[-3]
  # print line
  # print inputs


  return (make_coms(coms), make_opps(opps), invs)
  

def combine(combs, exists, dicto):

  # print exists
  # print dicto
  

  if len(exists) == 1:
    # dicto[exists[0]] = 1                #
    pass
  else:
    e1 = exists[-1]
    e2 = exists[-2]


    if e2 in combs[e1]:
      e3 = combs[e1][e2]
    else:
      e3 = -1


    if e3 != -1:
      dicto[e1] -= 1
      # if dicto[e1] == 0:
      #   dicto.pop(e1)
        
      dicto[e2] -= 1
      # if dicto[e2] == 0:
      #   dicto.pop(e2)
      if e3 in dicto:
        dicto[e3] += 1
      else:
        dicto[e3] = 1

      # print exists, e3, exists[:-2]
      exists = exists[:-2]
      exists.append(e3)
      # print exists, 'call'
      return combine(combs, exists, dicto)
      
  return (exists, dicto)

def reduct(opposites, exists, dicto):
  e = exists[-1]

  for o in opposites[e]:
    if o in dicto:
      if dicto[o] > 0:
        return ([], {})

  return (exists, dicto)
    
def solve(line):
  (combinations, opposites, invocations) = parse(line)
  # print combinations,'\n', opposites,'\n', invocations
  # print invocations

  exists = []
  dicto = {}

  for i in invocations:
    # print i, exists
    exists.append(i)
    if i in dicto:
      dicto[i] += 1
    else:
      dicto[i] = 1

    (exists, dicto) = combine(combinations, exists, dicto)
    (exists, dicto) = reduct(opposites, exists, dicto)


  return exists

def print_answer(i, ans):
  ans = filter(lambda x: x != "'", str(ans))
  return "Case #{0}: {1}\n".format(1+i, ans)

def solve_file(filename):
  out_name = filename[:-2]+"out"
  ins = open(filename, 'r')
  outs = open(out_name, 'w')

  ins.readline()

  for i, line in enumerate(ins):
    outs.write(print_answer(i, solve(line)))

  ins.close()
  outs.close()
