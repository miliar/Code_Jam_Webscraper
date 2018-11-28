readFile = open("A-large.in")
testCases = eval(readFile.readline())
ans = {}
for t in range(0,testCases):
    smax,string = map(str, readFile.readline().split())
    count = 0
    noOfPeople = eval(string[0])
    smax = eval(smax)
    for s in range(1,smax+1):
        if noOfPeople < s:
            count += 1
            noOfPeople += 1
        noOfPeople += eval(string[s])
    ans[t] = count

outputFile = open("StaningOvation.txt",'w')
for i in range(0,len(ans)):
    outputFile.write("Case #%d: %d\n" % (i+1,ans[i]))

readFile.close()
outputFile.close()
