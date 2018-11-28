def friendsNeed (audience, eachLevel):
    sumLevel = int(eachLevel[0])
    friendNeed = [0]
    for i in range (1, audience+1):
        if i>sumLevel:
            friendNeed.append(i-sumLevel)
        sumLevel = sumLevel + int(eachLevel[i])
    return max(friendNeed)

f = open('A-large.in', 'r')
fw = open('A-large.out', 'w')
testCases = int(f.readline())
for j in range (testCases):
    line = f.readline()
    list = line.split()
    audience = int(list[0])
    eachLevel = str(list[1])
    result = 'Case #' + str(j+1) + ': ' + str(friendsNeed(audience,eachLevel))+'\n'
    fw.write(result)






