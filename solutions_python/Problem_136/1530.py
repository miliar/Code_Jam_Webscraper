fileopen=open(r'K:\Codes\code jam solutions\2014 Round 1\Problem B Cookie Clicker\B-small-attempt3.in')
resultopen=open(r'K:\Codes\code jam solutions\2014 Round 1\Problem B Cookie Clicker\Prob B Output 2.txt', 'w')
index=-1
for value in fileopen:
    print value
    exiter=seconds=least=total=balance=flag=float(0)
    if index>=0 :
        c,f,x=(value[:-1].split(" "))
        c,f,x=float(c),float(f),float(x)
        print c,f,x
        prod=2.0
        if c<x: 
            while exiter==0:
                seconds+=float("%0.07f"%(c/prod))
                prod+=f
                total+=c
                val=float (float("%0.07f"%(x/prod))+seconds)
                if val<least or flag==0:
                    least=val
                if val>least:
                    exiter=1
                flag=1
                #print least
                #print "%0.02f"%least,"%0.02f"%prod,"%0.02f"%(x/prod),"%0.02f"%seconds,x
            if flag==0:
                least= float("%0.07f"%(x/prod))
        elif x<=c:
            least=float("%0.07f"%(x/2.0))
        least1 = float("%0.07f"%(x/2.0))
        if (least1 < least):
            least = least1 
        print "%0.07f"%least
        resultopen.write("Case #"+str(index+1)+": "+str("%0.07f"%least)+"\n")
    index+=1
fileopen.close()
resultopen.close()
