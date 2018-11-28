f = open('/home/rakesh/Desktop/codeJam/A-large (1).in', 'r')
fout = open('/home/rakesh/Desktop/codeJam/A-large-attempt_output.in', 'w')
counter=0
testCases=0
for line in f:
    line.rstrip()
    #print line
    if(counter==0):
        testCases=int(line)
        counter+=1
        continue
    frnds=0
    input=line.split()
    string=input[1]
    perStand=0
    for i in range(int(input[0])+1):
        addfrnd=0
        if(string[i]=='0'):
            continue
        if(i>perStand):
            addfrnd=i-perStand
            frnds+=addfrnd
        perStand=addfrnd+perStand+int(string[i])
    
    #print "added Friends",frnds
    outputstr="Case #%d: %d\n"%(counter,frnds)
    print outputstr
    fout.write(outputstr)
    counter+=1
            
    