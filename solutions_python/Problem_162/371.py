fil=open("C:\Users\Sharad Boni\Downloads\A-small-attempt1.in")
t=int(fil.readline().strip("\n"))
f=open("C:\Users\Sharad Boni\Desktop\srcoutput.txt","w")

for bd in xrange(t):
    
    ans=0
    n=int(fil.readline().strip("\n"))
    no=n

    while no>=1:
        n1=int((str(no))[::-1])
        if n1<=9:
            n1=no
        if no<=n1 :
            no-=1
                
        else:
            no=n1   
        ans+=1      
         
                                  
    print "Case #"+str(bd+1)+": "+str(ans)
    f.write("Case #"+str(bd+1)+": "+str(ans)+"\n")
         
    