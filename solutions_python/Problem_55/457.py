from collections import deque


f = open('C-small-attempt0.in','r')
w = open('output.txt', 'w')

cases = f.readline()
cases = int(cases)

for i in range(0, cases):
    groupsAdded = 0
    sumGroup = 0
    totalGroup = 0
    
    line = f.readline()
    arr = str.split(line, " ")
    
    R = int(arr[0])
    k = int(arr[1])
    N = int(arr[2])
    
    myQ = deque()
    
    line = f.readline()
    arr = str.split(line, " ")
    
    for j in range(0, N):
        myQ.append(int(arr[j]))
        
    for l in range(0, R):
        groupsAdded = 0
        sumGroup = 0
        
        while sumGroup <= k and groupsAdded < N:
            currentGroup = myQ.popleft()
            if currentGroup + sumGroup <= k:
                sumGroup = sumGroup + currentGroup
                myQ.append(currentGroup)
                groupsAdded = groupsAdded + 1
            else:
                myQ.appendleft(currentGroup)
                break
            totalGroup = totalGroup + currentGroup
    
    w.write("Case #" + str(i+1) + ": " + str(totalGroup) + "\n")

print "DONE"