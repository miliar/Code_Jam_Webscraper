import glob
for fname in glob.glob("*.in"):
    fp=open(fname)
    result=[]
    for i in range(int(fp.readline())):
        input=fp.readline()
        #input=[[x.split()[0],int(x.split()[1])] for x in input[input.find(" "):].split(",")]
        input1=input.split()
        input=[]
        for x in range(int(input1[0])):
            input.append([input1[1+x*2],int(input1[2+x*2])])
        Olast=Blast=1
        O=B=0
        buttonlast=None
        for x in input:
            if x[0]=="O":
                O=O+abs(x[1]-Olast)+1
                Olast=x[1]
                if buttonlast=="B" and B>=O:
                    O=B+1
                buttonlast="O"
            elif x[0]=="B":
                B=B+abs(x[1]-Blast)+1
                Blast=x[1]
                if buttonlast=="O" and O>=B:
                    B=O+1
                buttonlast="B"
        result.append("Case #%i: %s"%(i+1,O if O>B else B))
        print result
    fp.close()
    fp=open(fname[:fname.rfind(".")]+".out","w+")
    print result
    fp.write("\n".join(result))
    fp.close()