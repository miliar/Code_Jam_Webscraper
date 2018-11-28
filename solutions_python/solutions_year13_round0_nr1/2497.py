from sympy.matrices import *
if __name__ == '__main__':

    f = open("/home/devil/opc/A-large.in",'r')
    line = f.readline()
    T = int(line)
    t = 0
   
    
    lines = [line.strip('\n') for line in f]
    for line in lines:
        if(line==''):
            lines.pop(lines.index(line))
        
    f.close()
    f = open("bar.txt",'w')
    while t<T:
        A = Matrix([[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]])
        B = Matrix([[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]])
        C = Matrix([[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]])
        for i in range(4):
            l = lines[(4*t+i)]
            for j in range(4):
                ch = l[j]
                if ch == '.' or ch=='X':
                    A[i,j] = 0
                if ch == 'O' or ch=='.':
                    B[i,j] = 0   
                if ch == '.':
                    C[i,j] = 0     
              
        t+=1
        s=0
        q=0
        z=0
        for h in range(4):
            s+=A[h,3-h]
        if(s==34 or sum(A[:,0])==34 or sum(A[:,1])==34 or sum(A[:,2])==34or sum(A[:,3])==34):
            q=1;
        elif(sum(A[0,:])==34 or sum(A[1,:])==34 or sum(A[2,:])==34or sum(A[3,:])==34 or A.trace()==34):
            q=1;                     
        
        if(q==1):
            nn = "Case #%d: O won\n" %t
            f.write(nn)
       
        elif(q==0): 
          s=0
          for hh in range(4):
            s+=B[hh,3-hh] 
        
          if(s==34 or sum(B[:,0])==34 or sum(B[:,1])==34 or sum(B[:,2])==34or sum(B[:,3])==34):
            z=1;
           
          elif(sum(B[0,:])==34 or sum(B[1,:])==34 or sum(B[2,:])==34or sum(B[3,:])==34 or B.trace()==34):
            z=1;
                                 
          if(z==1):
             
             nn = "Case #%d: X won\n" %t
             f.write(nn)
        
        if(z==0 and q==0):
           if(sum(C)==136):
             nn = "Case #%d: Draw\n" %t
             f.write(nn)
           else:    
             nn = "Case #%d: Game has not completed\n" %t
             f.write(nn)
                 
    f.close()          
        
            
    
  
