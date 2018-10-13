f=open("A-small.in","r")
g=open("magic.out","w")

T = int(f.readline())

for i in range(0,T):

  a = int(f.readline())
  L1 = []
  for j in range(0,4):
    aux = map(int, f.readline().split())
    L1.append(aux)  
  
  b = int(f.readline())
  L2 = []
  for j in range(0,4):
    aux = map(int, f.readline().split())
    L2.append(aux)  
  
  check = []  
  for x in L1[a-1]:
    if x in L2[b-1]:
      check.append(x)

  if len(check) == 0:
    ans = 'Volunteer cheated!'
  elif len(check) == 1:
    ans = str(check[0])
  else:
    ans = 'Bad magician!'  

  g.write("Case #"+str(i+1)+": "+ans+"\n")

  
  
  
