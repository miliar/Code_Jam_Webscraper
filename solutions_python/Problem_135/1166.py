

inFile = open("A-small-attempt0.in")
outFile = open("A-small.out","w")

T = inFile.readline()
T = int(T)

for num in range(0,T):
    
    c1 = float(inFile.readline())
    m1 = [[0 for x in range(4)] for x in range(4)]
    line = inFile.readline()
    m1[0] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m1[1] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m1[2] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m1[3] = [float(x) for x in line.split(" ")];
    print( m1);
    
    c2 = float(inFile.readline())
    m2 = [[0 for x in range(4)] for x in range(4)]
    line = inFile.readline()
    m2[0] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m2[1] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m2[2] = [float(x) for x in line.split(" ")];
    line = inFile.readline()
    m2[3] = [float(x) for x in line.split(" ")];
    print (m2)
    
    card = 0
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            print(str(c1)+":"+str(i)+"::"+str(c2)+":"+str(j))
            ci1 = int(c1)
            ci2 = int(c2)
            

            if (int(m1[ci1-1][i]) == int(m2[ci2-1][j])):
                if (count == 0):
                    card = m1[ci1-1][i]
                count += 1
                
    
    if (count == 1):
        outFile.write("Case #"+str(num+1)+": "+str(int(card))+"\n")
    elif (count == 0):
        outFile.write("Case #"+str(num+1)+": Volunteer cheated!\n")
    else:
        outFile.write("Case #"+str(num+1)+": Bad magician!\n")
    #    outFile.write("Case #"+str(num+1)+": "+str(countD)+" "+str(countN)+"\n")

#inFile.close();#
#outFile.close();