f=open("A-small.in","r")
fout=open("A-small.out","w")
ncases=int(f.readline())
for c in range(ncases):   
    caso=(f.readline()).split()
    #print(caso)
    l=int(caso[0]) #len(v)
    s=caso[1]
    lungs=len(caso[0])
    v=[int(s[x:x+lungs]) for x in range(0,l+1,lungs)]
    print("vett",v)
    p=0
    sum=0
    stable=[]
    stable.extend([None]*(l+1))
    for i in range(l+1):
        if( i == 0):
            stable[0]=v[0]
        else:
            sum=0
            if(i>stable[i-1]):
                sum=i-stable[i-1]
                stable[i]=stable[i-1]+sum+v[i]
                p+=sum
            else:
                stable[i]=stable[i-1]+v[i]
                
    s="Case #"+str(c+1)+": "+str(p)
    print(s)
    fout.write(s+"\n")
fout.flush()
fout.close()