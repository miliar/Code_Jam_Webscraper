fil=open("C:\Users\Sharad Boni\Downloads\C-small-attempt3.in")
t=int(fil.readline().strip("\n"))
dic={"11":"1","1i":"i","1j":"j","1k":"k","i1":"1","ii":"-1","ij":"k","ik":"-j","j1":"j","ji":"-k","jj":"-1","jk":"i","k1":"k","ki":"j","kj":"-i","kk":"-1","i":"i","j":"j","k":"k","-11":"-1","-1i":"-i","-1j":"-j","-1k":"-k","-i1":"-1","-ii":"1","-ij":"-k","-ik":"j","-j1":"-j","-ji":"k","-jj":"1","-jk":"-i","-k1":"-k","-ki":"-j","-kj":"i","-kk":"1"}
f=open("C:\Users\Sharad Boni\Desktop\srcoutput.txt","w")
for i in xrange(t):
    l,r=fil.readline().strip("\n").split()
    l=int(l)
    r=int(r)
    s=r*(fil.readline().strip("\n"))
    flag1=0
    flag2=0
    flag=0
    x=""
   
    
    for en,a in enumerate(s):
        
        x=dic[x+a]
 
        if x=="i" or flag1==1:
            if flag1==0:
                flag1=1
                x=""
            if x=="j" or flag2==1:
                if flag2==0:
                    flag2=1
                    x=""
                if x=="k":
                    if en==len(s)-1:
                        flag=1
                        
                        
                
        
                        
    if flag==1 :
        f.write("Case #"+str(i+1)+": YES"+"\n")
        print("Case #"+str(i+1)+": YES")     
    else :
        f.write("Case #"+str(i+1)+": NO"+"\n") 
        print("Case #"+str(i+1)+": NO")    