import numpy as np
#myarray = np.asarray(mylist)

f = open('D-small-attempt4.in', 'r')
out = open('out1', 'w')
T=0
N=0
count=0
case=0
sum=0;
Win="GABRIEL"

#f.readline()
for line in f:

    if(count==0):	#T
        T=int(line.split()[0])
		#print(T)
    else:
        #case=case+1
        L=line.split()
        Array = [int(i) for i in L]
        if(Array[0]==1):
            Win="GABRIEL"
            
        elif(Array[0]==2):
            if((Array[2]*Array[1])%2==0):
                Win="GABRIEL"
            else:   
                Win="RICHARD"                
        elif(Array[0]==3):
            if(((Array[2]*Array[1])==6 )or ((Array[2]*Array[1])==9)or ((Array[2]*Array[1])==12)):
                Win="GABRIEL"
            else:
                Win="RICHARD"            
        elif(Array[0]==4):
            if((Array[2]*Array[1]==12) or( (Array[2]*Array[1])==16)):
                Win="GABRIEL"
            else:
                Win="RICHARD"
            # if((Array[2]*Array[1])%Array[0]==0):
                # Win="GABRIEL"
            # else:
                # Win="RICHARD"
        S='Case #'+str(count)+': '+Win+'\n'
        out.write(S)
    count=count+1   