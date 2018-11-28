f=open("/home/anurag/Downloads/A-large.in",'r')
o=open("out.txt",'w')

T=int(f.readline())

for p in range(T):
    N = int(f.readline().split()[0])
    ans = 0
    l = []
    for i in range(N):
        x = f.readline().split()
        
        present = (int(x[0]),int(x[1]))
        for j in range(len(l)):
            if present[0] < l[j][0] and present[1] > l[j][1]:
                ans += 1
            elif present[0] > l[j][0] and present[1] < l[j][1]:
                ans += 1
                

        l.append((int(x[0]),int(x[1])))
    o.write("Case #%d: %d\n" %(p+1,ans))
      
        
            
                       
            
                  
        
  
