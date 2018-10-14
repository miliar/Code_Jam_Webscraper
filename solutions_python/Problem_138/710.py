#Decietful war
#small and Large input supporting

def fairPointsGenerator(naomi,ken):
  points = 0
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
      points += 1
      for i in range(len(ken)-1,-1,-1):
	if used[i] == False:
	  used[i] = True
	  break
  return points
  
def decietpointsGenerator(naomi,ken):
  points = 0
  naomi.reverse()
  ken.reverse()
  bp_naomi = 0
  max_naomi = len(naomi)
  bp_ken = 0
  max_ken = len(ken)
  while bp_naomi<max_naomi:
    if naomi[bp_naomi] > ken[bp_ken]:
      points+=1
      bp_naomi +=1
      bp_ken +=1
    else:
      max_naomi -=1
      bp_ken +=1     
  return points
  
    
f = open("output.txt","w")
t = int(raw_input())
for i in range(0,t):
  n = int(raw_input())
  naomi = list(map(float,raw_input().split()))
  ken = list(map(float,raw_input().split()))
  naomi.sort()
  ken.sort()
  fair = fairPointsGenerator(naomi,ken)
  deciet = decietpointsGenerator(naomi,ken)
  f.write("Case #"+str(i+1)+": "+str(deciet)+" "+str(fair)+"\n")
  print fair,deciet
f.close()