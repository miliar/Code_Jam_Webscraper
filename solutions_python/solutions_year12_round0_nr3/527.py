#author: Stanisław Kacprzak

cache=dict()
def initCache():
    inputFile=open('lookUp.txt','r')
    for line in inputFile.readlines():
        numbers=line.split(" ")
        recs=list()
        for rec in numbers[1:]:
            recs.append(int(rec))
        cache[int(numbers[0])]=recs
    inputFile.close()
    print("cache load")
              
def recycleNumbersCount(num,b):    

    recycled=cache[num]
    ans=0;
    for rec in recycled:
        if rec > num:
            if rec <= b:
                ans+=1
            else:
              break
    return ans
    
inputFile=open('input2.txt','r')
outputFile=open('output.txt','w')
initCache()
lineNumber=int(inputFile.readline())
for n in range(1,lineNumber+1):
    testCase=inputFile.readline()
    integers=testCase.split(' ')
    a=int(integers[0])
    b=int(integers[1])
    answer=0
    for num in range(a,b):
        answer+=recycleNumbersCount(num,b)
    outputFile.write("Case #" + str(n) + ": " + str(answer)+"\n")
    print("Case #" + str(n) + ": " + str(answer))
outputFile.close()
