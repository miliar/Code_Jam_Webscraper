InFile = open('A-large.in','r')
OutFile = open('Output.out','w')

T = int(InFile.readline().rstrip('\n'))

for i in range(T):

    line = InFile.readline().rstrip('\n').split(' ')

    Smax = int(line[0])
    Pis = line[1]
    
    if Smax == 0:
        OutFile.write('Case #'+str(i+1)+": "+str(0)+'\n')

    else:
        nePeople = 0
        upPeople = 0 
        for Si in range(0,Smax+1):
            auPeople = int(Pis[Si])
            if upPeople < Si:
                nePeople = nePeople + Si - upPeople
                upPeople = Si
            upPeople = upPeople + auPeople

        OutFile.write('Case #'+str(i+1)+": "+str(nePeople)+'\n')
        

InFile.close()
OutFile.close()
