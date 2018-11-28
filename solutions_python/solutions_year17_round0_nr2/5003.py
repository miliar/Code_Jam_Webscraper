
t=int(raw_input())
winner=''
for j in xrange(1,t+1):
  N=[int(s) for s in raw_input().split(" ")]
  for i in xrange(1,N[0]+1):
      t=str(i);
      if len(t)==1:
              winner=t
              continue
      for x in xrange(1,len(t)):
          if int(t[x-1])<=int(t[x]) :
              if int(t[x])==int(t[len(t)-1]):
                  winner=t
              continue    
          else:
              break
  print("case #"+str(j)+": "+str(winner))

        
