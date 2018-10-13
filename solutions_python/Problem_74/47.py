import string
fin=open("A-large.in",'r')
T = int(fin.readline())
result=[]
outfile=open("output.txt","w")
for case in range(1,T+1):
    line0 = fin.readline()
    content=line0.split()
    number=int(content[0])
    task=[]
    for i in range(1,number+1):
        task.append((content[2*i-1],int(content[2*i]))) 
    stepO=0
    positionO=1
    stepB=0
    positionB=1
    flag=""
    for i in task:
        if i[0]=="B":
            if flag=="B":
                step=abs(positionB-i[1])
                stepB=stepB+1+step
                positionB=i[1]
            else:
                step=abs(positionB-i[1])
                stepB1=stepB+1+step
                stepB2=stepO+1
                stepB=max(stepB1,stepB2)
                positionB=i[1]
            flag="B"
        else:
            if flag=="O":
                step=abs(positionO-i[1])
                stepO=stepO+1+step
                positionO=i[1]
            else:
                step=abs(positionO-i[1])
                stepO1=stepO+1+step
                stepO2=stepB+1
                stepO=max(stepO1,stepO2)
                positionO=i[1]
            flag="O"
    f_str=max(stepO,stepB)
    f_str="Case #%d: %d \n" % (case,f_str)
    outfile.write(f_str)
outfile.close()            
print "done"
