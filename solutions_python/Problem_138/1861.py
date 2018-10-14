import copy

def war_optimal (naomi, ken):
  naomi1 = copy.copy(naomi)
  naomi1.sort()
  naomi.sort()

  ken1 = copy.copy(ken)
  ken1.sort()
  ken.sort()
  
  points = 0
  for i in naomi:
    found = False
    for j in ken1:
      # the first found will be 
      if j > i:
        naomi1.remove(i)
        ken1.remove(j)
        found = True
        break
    if not found :
      #enter here if no larger from ken, pick the smallest one
      naomi1.remove(i)
      ken1.pop(0)
      points += 1
  return points

def min(a):
  minValue = 1.0
  for x in a:
    if x < minValue:
      minValue = x
  return minValue

def max(a):
  maxValue = 0.0
  for x in a:
    if x > maxValue:
      maxValue = x
  return maxValue

def checkDone(naomi, ken):
    if min(naomi) > min(ken):
      return len(naomi)
    else:
      return 0

def deceitful_war (naomi, ken,count=0):
  #sort from small to large
  if len(naomi)==0:
    return count
  naomi1 = copy.copy(naomi)
  #sort from small to large
  ken1 = copy.copy(ken)
  # get as many big one out as possible from Ken
  for a in naomi:
    if a < min(ken1):
      naomi1.remove(a)
      ken1.remove(max(ken1))
      return deceitful_war(naomi1,ken1,count)
  # need to remove all the big ones from Kens as long as it's bigger than
  # Naomi's max
  naomi1.remove(min(naomi1))
  ken1.remove(min(ken1))
  return deceitful_war(naomi1,ken1,count+1)

  return points

testNumbers = 0
with open ("D-small-attempt2.in") as testFile:
  testNumbers= int(testFile.readline())
  for index in range(0, testNumbers):
    NumberOfBlocks = int(testFile.readline().split()[0])
    #print NumberOfBlocks
    NaomiBlocks = []
    NaomiBlocks = testFile.readline().split()
    KenBlocks = []
    KenBlocks = testFile.readline().split()
    #print NaomiBlocks
    #print KenBlocks
    #print "\n\n"

    NaomiBlocksFloat = []
    KenBlocksFloat = []

    for b in NaomiBlocks:
      NaomiBlocksFloat.append(float(b))
    for b in KenBlocks:
      KenBlocksFloat.append(float(b))
    NaomiBlocksFloat.sort()
    KenBlocksFloat.sort()
    #print NaomiBlocksFloat
    #print KenBlocksFloat
    print "Case #%d: %d %d" % ((index + 1), deceitful_war(NaomiBlocksFloat, KenBlocksFloat), war_optimal(NaomiBlocksFloat, KenBlocksFloat))
