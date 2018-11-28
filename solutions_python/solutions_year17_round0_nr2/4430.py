import sys

def calcul(t):
    nb=int(t)
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i]>t[j]:
                return(calcul(str(nb-1)))
    return(nb)
case=1
nb_de_pb=int(sys.stdin.readline().split()[0])
for p in range(nb_de_pb):
  z="Case #"+str(case)+": "
  case+=1
  l=[]
  t=sys.stdin.readline().split()[0]
  nb=calcul(t)
  print(z+str(nb))
