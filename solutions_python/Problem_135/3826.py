import collections

def MagicTrick():
  f_in = open('A-small-attempt0.in', 'rU')
  f_out = open('A-small-attempt0.out', 'w')
  lines = f_in.readlines()
  f_in.close()
  numCases = int(lines[0])
  counter = 1
  results = []
  for i in range(1, numCases+1):
    case = []
    for x in range(0, 10):
      case.append(lines[x+counter])
    result = "Case #" + str(i) + ": " + MagicCase(case) + "\n"
    f_out.write(result)
    counter += 10
  f_out.close()
   
def MagicCase(case):
  guess1 = int("".join(case[0].strip()))
  guess2 = int("".join(case[5].strip()))

  cards1 = collections.defaultdict(list)
  cards2 = collections.defaultdict(list)
  found = []
  
  for i in range(1,5):
    for n in case[i].split():
      cards1[i].append(n)
  for i in range(6,10):
    for n in case[i].split():
      cards2[i-5].append(n)
  
  for i in cards1[guess1]:
    if i in cards2[guess2]:
      found.append(i)
  

  if len(found) > 1:
  	return "Bad magician!"
  elif found:
    return str(found[0])
  else:
  	return "Volunteer cheated!"

MagicTrick()