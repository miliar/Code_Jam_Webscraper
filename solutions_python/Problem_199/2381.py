lis = []
for i in open('A-large.in'):
    lis.append(i.strip())
print(lis)
fOut = open('out1.txt', 'w')
caseSize = int(lis[0])

solList = []

def flip(pcks):
    outLis = []
    pcks = list(pcks)
    for val in pcks:
        if val == "-":
            outLis.append("+")
        else:
            outLis.append("-")


    return ''.join(outLis)



for case in lis[1:caseSize+1]:
    pancakes = case.split(" ")[0]
    panSize = int(case.split(" ")[1])

    pancakeList = list(pancakes)
    counter = 0
    for val in range(0, len(pancakes)-(panSize-1)):
        #print(val)
        focusList = []

        if pancakeList[val] == "-":
            for i in range(0, panSize):
                #print('b', pancakeList)
                pancakeList[val + i] = flip(pancakeList[val + i])
                #print('a', pancakeList)
            counter += 1
    if '-' in pancakeList:
        sol = "IMPOSSIBLE"
    else:
        sol = counter


    solList.append(sol)
    #print(sol)

for val in range(0,len(solList)):
    fOut.write("Case #" + str(val+1) + ": " + str(solList[val]) + "\n")
fOut.close()
