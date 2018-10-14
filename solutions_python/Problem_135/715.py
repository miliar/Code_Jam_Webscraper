fin = open("A-small-attempt0.in", 'r')
fout= open("out.txt", 'w')



count = 0
dictd = dict()

testCaNum= int(fin.readline().strip())
for testCa in range(1, testCaNum +1):
    fiList = []
    fch = int(fin.readline().strip())
    for num in range(1,5):
        fiList.append(fin.readline().strip().split())
    choic = fiList[fch-1]
    fch = int(fin.readline().strip())
    fiList = []
    for num in range(1,5):
        fiList.append(fin.readline().strip().split())
    sch = fiList[fch-1]
    j = 0
    for i in choic:
        if (i in sch):
            j=j+1
            n = i
    fout.write("Case #"+str(testCa)+": ")
    if(j == 0):
        fout.write("Volunteer cheated!\n")
    elif(j==1):
        fout.write(n+"\n")
    else:
        fout.write("Bad magician!\n")
        
fin.close()
fout.close()
