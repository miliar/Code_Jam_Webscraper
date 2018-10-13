
fp=open("B-small-attempt0.in","r")
fo=open("B-small-attempt0.out","w")
numberOfTest=fp.readline()
for testNumber in range(int(numberOfTest)):
    line=fp.readline()
    array=line.split()
    a=int(array[0])
    b=int(array[1])
    n=int(array[2])
    res=[]
    for i in range(a):
        for j in range(b):
            a=i&j
            if a<n:
                res.append(a)
        
    fo.write("Case #"+str(testNumber+1)+": "+str(len(res))+"\n")
fo.close()        
fp.close()
