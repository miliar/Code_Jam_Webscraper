#Decietful war

def getFairScore(naomi,ken):
  score = 0
  used = [False]*len(ken)
  for block in naomi:
    flag = 1
    for i in range(0,len(ken)):
      if ken[i] > block and used[i] == False:
	print "ken wins block "+str(block)+" with "+str(ken[i])
	used[i] = True
	flag = 0
	break
    if flag == 1:
      score += 1
      for i in range(len(ken)-1,-1,-1):
	if used[i] == False:
	  used[i] = True
	  break
  return score
  
def getDecietScore(naomi,ken):
  score = 0
  naomi.reverse()
  ken.reverse()
  bp_naomi = 0
  max_naomi = len(naomi)
  bp_ken = 0
  max_ken = len(ken)
  while bp_naomi<max_naomi:
    if naomi[bp_naomi] > ken[bp_ken]:
      score+=1
      bp_naomi +=1
      bp_ken +=1
    else:
      max_naomi -=1
      bp_ken +=1     
  return score
  
    
f = open("output.txt","w")
t = int(raw_input())
for i in range(0,t):
  n = int(raw_input())
  naomi = list(map(float,raw_input().split()))
  ken = list(map(float,raw_input().split()))
  naomi.sort()
  ken.sort()
  fair = getFairScore(naomi,ken)
  deciet = getDecietScore(naomi,ken)
  f.write("Case #"+str(i+1)+": "+str(deciet)+" "+str(fair)+"\n")
  print fair,deciet
f.close()