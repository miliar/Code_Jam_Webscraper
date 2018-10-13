numCases = input()
cases = []
numCases = numCases.split("\n")
del numCases[0]
j = 0
for i in numCases:

    l = 0
    for char in i:
        if char != " ":
            l += 1
        elif char == " ":
            break
    i = i[l+1:]
    cases.append(i)

caseNum = 1
for case in cases:
    numClap = 0
    numFriends = 0
    index = 0
    for char in case:
        clapped = False
        while clapped == False:
            if numClap >= index:
                numClap += int(char)
                clapped = True
            else:
                numFriends += 1
                numClap += 1
        index += 1
    print("Case #" + str(caseNum) + ": " + str(numFriends))
    caseNum += 1

            
        
        
