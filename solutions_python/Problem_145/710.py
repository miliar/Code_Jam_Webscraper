import math as m    
fil=open("tester.txt","w+")
fil2=open("A-small-attempt2.in","r")
testCases=int(fil2.readline())
for i in range(1,testCases+1):
    gene=0
    flag=0
    fraction=fil2.readline()
    frac=fraction.split("/")
    first=int(frac[0])
    second=int(frac[1])
    for j in range(1,first+1):
        if((second%j==0)&(first%j==0)):
            second=second/j
            first=first/j
    for j in range(0,41):
        if(second==(2**j)):
            flag=1
            if(first==1):
                gene=int(m.log(second,2))
            else:
                gene=gene+1
                while(first<(second/2)):
                    second=second/2
                    gene=gene+1

                        
        
    if(flag==0):
        fil.write('Case #%d: impossible\n'%(i))
    else:
        fil.write('Case #%d: %d\n'%(i,gene))
        

