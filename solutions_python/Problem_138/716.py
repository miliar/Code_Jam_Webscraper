import sys
import math

if len(sys.argv)<2:
  exit()
  
def kenchoose(c, naomitold, ken):
  flag = False
#  print "Told Naomi "+str(naomitold)
  
  for j in range(c):
    if naomitold < ken[j]:
#      print "removed 1 "+str(ken[j])
      kenchoose = ken[j]
      ken.remove(ken[j])
      flag = True
      break
    
  if not(flag):
#    print "removed 2 "+str(ken[0])
    kenchoose = ken[0]
    ken.remove(ken[0])

  return kenchoose
  
def playw(c, naomi, ken):
  r = 0
  naomi_c = list(naomi)
  ken_c = list(ken)
  for n in naomi_c:
    if n > kenchoose(c, n, ken_c):
      r+=1
    c-=1
  
  return r
  
def playd(c, naomi, ken):
#  print "\nPlayd"
  r = 0
  naomi_c = list(naomi)
  ken_c = list(ken)
  
#  print naomi_c
#  print ken_c
  
  while c>0:
    chosenNaomi = naomi_c[0]
    naomi_c.remove(chosenNaomi)
#    print "Chosen Naomi"+str(chosenNaomi)
    if chosenNaomi > ken_c[0]:
      toldNaomi = (1+ken_c[c-1])/2
    elif chosenNaomi < ken_c[c-1] and c>1:
      toldNaomi = (ken_c[c-1]+ken_c[c-2])/2
    else:
      toldNaomi = chosenNaomi
    
    if chosenNaomi > kenchoose(c, toldNaomi, ken_c):
      r+=1
      
    c-=1
#  print "end Playd\n\n"
  return r

fname = sys.argv[1]
fn = open(fname, "r")
n = int(fn.readline())

for i in range(0, n):
  c = int(fn.readline())
  naomi = [float(y) for y in fn.readline().split()]        
  ken = [float(y) for y in fn.readline().split()]        
  naomi = sorted(naomi)
  ken = sorted(ken)
  
  
  print "Case #%d: %d %d " % (i+1, playd(c, naomi, ken), playw(c, naomi, ken))
  

  

fn.close()

                                        
