file = open("B-small-attempt4.in", "r")

cases = int(file.readline())

finishedList = []

i = 0
while(i < cases):
    #get our number
    i += 1
    n = int(file.readline())
    n = str(n)
    
    #do calculations per number
    l = 0
    while(l < len(n)-1):
        if(n[l] > n[l+1]):
                
            #first line
            if(l == 0):
                if(int(n[l]) > 1):
                    n = str(int(n[l])-1) + ("9" * (len(n) - 1))
                    
                else:
                    n = "9" * (len(n) - 1)
                 
            #other lines
            else:
                
                if(n[l] > n[l-1]):
                    n = n[:l] + str(int(n[l])-1) + ("9" * (len(n) - (l+1)))
                else:
                    n = str(int(n[0]) - 1) + ("9" * (len(n) - 1))
        l += 1

    finishedList.append(n)


#write the answer file
print(finishedList)


outputFile = open("TidyNumbers.out", "w")

m = 1

while (m <= cases):

    outputFile.write("Case #" + str(m) + ": " + str(finishedList[m-1]) + "\n")
    m += 1

outputFile.close()
