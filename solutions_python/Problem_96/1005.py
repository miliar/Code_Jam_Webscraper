'''
Created on 14-04-2012

@author: Hokanos
'''
import sys
def main():
    f = open(sys.argv[1],"r")
    fw = open("out.out","w")
    n = int(f.readline())
    
    for i in range(n):
        v = f.readline().rstrip().split(" ")
        count = 0
        sup = int(v[1])
        p = int(v[2])
        #print(p)
        for j in range(3,len(v)):
            ptk = int(v[j])
            r = ptk%3
            x = int((ptk)/3)
            #print(ptk,x,r,sup)
            if ptk<p:
                continue
            
            if r==0:
                if x>=p:
                    count+=1
                    continue
                if sup > 0:
                    if x+1>=p:
                        sup -=1
                        count+=1
                        continue
            
            if r==1:
                if x+1>=p:
                    count+=1;
                    continue;
            
            if r==2:
                if x+1>=p:
                    count+=1
                    continue
                if sup > 0:
                    if x+2>=p:
                        sup -=1
                        count+=1
                        continue
            
                   
        #print()
        fw.write("Case #"+str(i+1)+": "+str(count)+"\n")  
        
    fw.close()
    f.close()         
#            r = ptk%3
#            x = int(ptk/3)
#            #print(ptk,x,r,sup)
#            if r == 0:
#                if x>=p:
#                    #print(ptk,x)
#                    count+=1;
#                    continue; 
#                if (x+1>=p):
#                    if sup != 0:
#                        sup -= 1
#                        count+=1;
#                        continue;
#            if r == 1:
#                if x+1 >= p:
#                    #print(ptk,x,r)
#                    count+=1;
#                    continue;
#                    
#            if r == 2:
#                if x+1 >= p:
#                    #print(ptk,x,r)
#                    count+=1;
#                    continue;
#                
#                if x+2 >= p:
#                    if(sup != 0):
#                        sup -= 1
#                        count+=1;
#                        #print(ptk,x,r,sup)
#                        continue;

            
        #print()
        #print(count)
    fw.close()
    f.close()
    
main()
                     