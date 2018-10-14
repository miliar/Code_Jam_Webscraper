import sys

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for case in range(size):

  iFile.readline()

  line = iFile.readline().strip().split()
  naomi = [float(a) for a in line]
  naomi.sort()
  
  line = iFile.readline().strip().split()
  ken = [float(a) for a in line]
  ken.sort()
  
  deceit_score = 0
  j = 0
  for i in range(len(naomi)):
    if naomi[i] > ken[j]:
      deceit_score += 1
      j += 1
  
  score = 0    
  i = 0
  for j in range(len(ken)):
    if ken[j] > naomi[i]:
      i += 1
    else:
      score += 1
      
  output = str(deceit_score)+" "+str(score)
  print("Case #"+str(case+1)+": "+output)
