import numpy as np
#myarray = np.asarray(mylist)

f = open('A-small-attempt0.in', 'r')
out = open('out1', 'w')
T=0
N=0
count=0
case=0
sum=0;

#f.readline()
for line in f:
    output=0
	#print (line)
	#reading the first line
    if(count==0):	#T
        T=int(line.split()[0])
		#print(T)
    else:
        #case=case+1
        L=line.split()
        N=int(L[0])
        STR=L[1]
        Array = [int(i) for i in STR]
        sum=0
        ppl=0
        x=0
        size=len(Array)
        for x in range(0, size):
            if Array[x]>0:
                if x > sum:
                    ppl=ppl+x-sum
                    sum=sum+ppl
            sum=Array[x]+sum
        S='Case #'+str(count)+': '+str(ppl)+'\n'
        out.write(S)
    count=count+1   