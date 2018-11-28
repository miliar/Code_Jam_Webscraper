infile=open('/home/akp/Desktop/round1/1.in', 'r')
outputfile= open('/home/akp/Desktop/round1/1.out','w')
testcase=infile.readline()
for j in range(int(testcase)):
    counter=0
    a,b,k=map(int, infile.readline().split())
    for i in range(0, a):
        for m in range(0,b):
            if i&m < k and i&m >=0:
                counter+=1
    outputfile.write( str('Case #'+ str(j+1) +': '+str(counter)+'\n'))            
                
                
    