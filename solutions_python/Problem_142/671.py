
def parseString(word):
  dico = []
  c = word[0]
  cpt = 0
  for i in xrange(len(word)):
    if c != word[i]:
      dico.append((word[i-1],cpt))
      cpt = 1
      c = word[i]
    else:
      cpt += 1
      c = word[i]
  dico.append((word[len(word)-1],cpt))
  return dico

def checkSize(tab):
  occ = len(tab[0])
  for i in xrange(len(tab)):
    if occ != len(tab[i]):
      return False   
  return True

def checkLetter(tab):
  sent = tab[0]
  for i in xrange(len(tab)):
    for j in xrange(len(tab[i])):
      if sent[j][0] != tab[i][j][0]:
        return False
  return True

def findInterval(tab):
  cpt = 0
  for i in xrange(len(tab[0])):
    t_max = 0
    t_min = 10000
    for j in xrange(len(tab)):
      if tab[j][i][1] > t_max:
        t_max = tab[j][i][1]
      if tab[j][i][1] < t_min:
        t_min = tab[j][i][1]
    cpt += (t_max - t_min)
  return cpt

######################################################
#### MAIN :)
######################################################

nb_case = int(raw_input())

for i in xrange(nb_case):
  nb_row = int(raw_input())
  res = []
  for j in xrange(nb_row):
    res.append(parseString(str(raw_input())))
  if checkSize(res):
    if checkLetter(res):
      print("Case #%d: %d" % (i+1,findInterval(res)))
    else:
      print("Case #%d: Fegla Won" % (i+1))
  else:
    print("Case #%d: Fegla Won" % (i+1))
  

