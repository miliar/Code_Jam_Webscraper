def co(C,F,X):   
    r=2
    t=0
    while (X-C)>((X*r)/(r+F)):
        t+=(C/r)
        r+=F    
    t+=X/r
    return t









def main(S):
    T=int(S[0])
    for y in range(0,T,1):
        print("")
        a=S[y+1].split(" ")
        print(("Case #"+str(y+1)+": "+str(co(float(a[0]),float(a[1]),float(a[2])))),end="")

        

S=input("Input")
S=S[3:-3]
S=S.split("\n")
main(S)










        
        
        

                
    
  
