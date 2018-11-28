fi = open("input.in")
fo = open("output.out", "w+")

totalCaseNum = int(fi.readline())

for i in range(1, totalCaseNum + 1):
    temp, data = fi.readline().split()
    currentPeople = 0
    friendNum = 0
    
    for j in range(len(data)):
        if currentPeople + friendNum < j:
            friendNum = j - currentPeople
        
        currentPeople += int(data[j])
        
    fo.write("Case #%d: %d" % (i, friendNum) + "\n")
    print(friendNum)
