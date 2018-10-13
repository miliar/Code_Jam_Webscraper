import string
f = open("C-small-attempt0.in")
fwrite = open('C-small-attempt0.out', 'w')
numCases = int(f.readline())
for i in range(0,numCases):
    numRecycled = 0
    nextLine = f.readline()
    nextLineArray = nextLine.split(' ')
    nextLineArray = map(int,nextLineArray)
    a = nextLineArray[0]
    b = nextLineArray[1]
    for j in range(a,b):
        originalI = [int(x) for x in str(j)]
        if(len(originalI) == 1):
            break
        recycledI = list(originalI)
        recycledI.insert(0,recycledI.pop())
        while(recycledI != originalI):
            jumbledNumber = int(''.join(map(str,recycledI)))
            for k in range(j,b+1):
                if jumbledNumber == k:
                    numRecycled += 1
            recycledI.insert(0,recycledI.pop())
    fwrite.write("Case #" + str(i+1) + ": " + str(numRecycled) +'\n')
f.close()
fwrite.close()
