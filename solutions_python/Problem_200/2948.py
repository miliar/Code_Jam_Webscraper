with open ('B-small-attempt0.in', 'r') as input,open('sampalo.txt','w') as output:
  x=input.readline()
  for i in range(1,int(x)+1):
    n=input.readline()
    n=int(n)
    while str(n)!=''.join(sorted(str(n))):
      n=n-1
    output.write('Case #'+str(i)+': '+str(n)+"\n")  
