import math
foo=open("A-s-0.in",'r')
bar = open("output.txt",'w')


n = int(foo.readline().rstrip())
i=1

while i<=n :
    line=foo.readline().rstrip().split()
    r=int(line[0])
    t=int(line[1])
   

    a = r*2 +1
    
    d = math.sqrt((2*a - 4)**2 + (32*t))

    n1 = (-(2*a - 4) + d)/8.0
 
    

    print int(n1),n1
  
    ans="Case #"+str(i)+": "+str(int(n1))+'\n'
     
    bar.write(ans)        

    i+=1
foo.close()
bar.close()

        
    

