InputFile="C:/Users/Vinit Gandhi/Desktop/A-small-attempt1.in"
OutputFile="C:/Users/Vinit Gandhi/Desktop/Output1.txt"
In=open(InputFile,'r')
Out=open(OutputFile,'w')
x=int(In.readline().rstrip())
for _ in xrange(x):
    a,b=(In.readline().rstrip().split())
    count=add=0
    for index,char in enumerate(b):
        if index<=count:
            count+=int(char)
        elif int(char):
            add+=(index-count)
            count+=(add + int(char))
    Out.write(str("Case #"+str(_+1)+": " + str(add) + "\n"))
In.close()
Out.close()
              
            
        
        
