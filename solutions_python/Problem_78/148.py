import sys
import functools
def toInt(x):
  return int(x)

def new_matrix(L,C,num):
  return [[num for row in range(C)] for col in range(L)] #@UnusedVariable

file = open('mandar.txt','w')
sys.stdout = file

input  = open('../../input/a.in')
CASES  = int(input.readline())
for case in range(CASES):
  args = map(toInt,input.readline().rstrip().split(' '))
  N=args[0]
  D=args[1]
  G=args[2]
  fD = float(D)/100
  res='Broken'
  if D<100 and G==100:
    res='Broken'
  elif D>0 and G==0:
    res='Broken'
  elif D==0:
    res='Possible'
  elif fD*N<1:
    res='Broken'
  else:
    fac5=0
    d5=D
    while fac5<2:
      if d5%5==0:
        d5=D/5
        fac5+=1
      else:
        break
    
    fac2=0
    d2=D
    while fac2<2:
      if d2%2==0:
        d2=D/2
        fac2+=1
      else:
        break
    mult5 = 5**(2-fac5)
    mult2 = 2**(2-fac2)
    if N>=mult2*mult5:
      res = 'Possible'
    else:
      res='Broken'
  
  print 'Case #'+str(case+1)+': '+res
   
