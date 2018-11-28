import fileinput

def processCase(numcase, thiscase):
  first_set = set(thiscase['first_cards'][thiscase['first_answer']-1])
  second_set = set(thiscase['second_cards'][thiscase['second_answer']-1])
  
  result = list(first_set & second_set)

  if len(result) == 0:
    txt = "Volunteer cheated!"
  elif len(result) > 1:
    txt = "Bad magician!"
  else:
    txt = str(result[0])

  print "Case #%d: %s" % (numcase, txt)



testCases = []

i=0
for line in fileinput.input():
  if i == 0:
    readCases = int(line)
    j=0
    h=0
  else:
    if j >= readCases:
      break

    if h == 0:
      testCases.append({})
      testCases[j]['first_cards'] = []
      testCases[j]['second_cards'] = []
      testCases[j]['first_answer'] = int(line)
    elif h < 5:
      cards = line.strip('\n').split(' ')
      testCases[j]['first_cards'].append(map(lambda x: int(x), cards))
    elif h == 5:
      testCases[j]['second_answer'] = int(line)
    elif h > 5:
      cards = line.strip('\n').split(' ')
      testCases[j]['second_cards'].append(map(lambda x: int(x), cards))

    h+=1
    if h > 9:
      j+=1
      h=0

  i+=1

i=0
for case in testCases:
  i+=1
  processCase(i, case)