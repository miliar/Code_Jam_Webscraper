fk=open("input.txt","r")
f2=open("output.txt","w")
T=int(fk.readline())
for l in range(1,T+1):
 a,b,k=[int(x) for x in fk.readline().split()]
 count=0
 i=0
 while i<a:
        j=0
        while j<b:
            if(i&j<k):
                count+=1
            j+=1
        i+=1       
 f2.write("Case #"+str((l))+": "+str(count)+"\n") 
