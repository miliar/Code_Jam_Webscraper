memo = {}

def checkIfFinished(arr):
   for i in range(len(arr)):
        if arr[i] > 0:
           return False
   return True
 
def simulateMin(arr):
    hasharr = hash(str(arr))
    if hasharr in memo:
        return memo[hasharr]
    if checkIfFinished(arr):
        return 0 #CHECK
    notspecial=list(arr)
    for i in range(len(notspecial)):
        if notspecial[i] != 0:
            notspecial[i] = notspecial[i] - 1
    special=list(arr)
    special2=list(arr)
    maxplates = max(special)
    if maxplates > 2:
        for i in range(len(special)):
            if special[i] == maxplates:

                el = special[i] 
                partition1 = el/2
                partition2 = el - partition1
                special[i] = partition1
                special.append(partition2)
                if special2[i] % 2  != 0 and maxplates > 5:
                    partition1 = el/2 - 1
                    partition2 = el - partition1
                    special2[i] = partition1
                    special2.append(partition2)
                    memo[hasharr] = min(simulateMin(special)+1, simulateMin(notspecial)+1, simulateMin(special2)+1)
                    return memo[hasharr]
                break
        memo[hasharr] = min(simulateMin(special)+1, simulateMin(notspecial)+1)
        return memo[hasharr]
    memo[hasharr] = simulateMin(notspecial)+1
    return memo[hasharr]


f = open('/home/ben/Downloads/B-small-attempt9.in', 'r')
output = open('/home/ben/Documents/python/outputb', 'w')
T = int(f.readline())
newline=''
for case in range(T):
    DinersNo = int(f.readline())
    D = map(int, f.readline().split())
    output.write(newline + "Case #" + str(case+1) + ": " + str(simulateMin(D)))
    newline = '\n'
output.close()    
f.close()
