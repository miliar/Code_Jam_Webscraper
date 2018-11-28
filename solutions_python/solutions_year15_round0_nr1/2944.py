fin = open("A-large.in", 'r')
fout= open("out.txt", 'w')



count = 0
dictd = dict()

testCaNum= int(fin.readline().strip())
for testCa in range(1, testCaNum +1):
    fiList = []
    fch = fin.readline().strip().split()
    li = list(fch[1])
    #print(fch)
    acc=li[0]
    for i in range(len(li)):
        li[i]=int(li[i])
    acc=li[0]
    friends = 0
    for i in range(1,len(li)):
        #print(acc,friends)
        if li[i] > 0:
            if i <= acc:
                acc = acc+ li[i]
            else:
                friends = friends + (i - acc)
                acc = i + li[i]
    
    fout.write("Case #"+str(testCa)+": "+ str(friends)+"\n")
    #if(j == 0):
        #fout.write("Volunteer cheated!\n")
    #elif(j==1):
        #fout.write(n+"\n")
    #else:
        #fout.write("Bad magician!\n")
        
fin.close()
fout.close()
