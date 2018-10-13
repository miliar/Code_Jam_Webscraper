def feasible(a,b,c):
    i=1
    while i<=b:
          j=0
          while j<=i:
               if (j*100)%i==0 and (j*100)/i==c:
                  return 1
               j+=1
          i+=1
    return 0 
T1=raw_input()
T=int(T1)
i=1
while i<=T:
      k=0
      inp=raw_input().split()
      N=int(inp[0])
      p_d=int(inp[1])
      p_g=int(inp[2])
      if p_d>0 and p_g==0: 
         print "Case #%d: Broken" %i
      elif p_d<100 and p_g==100:
         print "Case #%d: Broken" %i
      else:
         k=feasible(0,N,p_d)
         if k==1: 
            print "Case #%d: Possible" %i  
         else:
            print "Case #%d: Broken" %i
      i+=1
                     
            
