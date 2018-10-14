

def getLastPerson(n, people):

    nums = []
    for i in range(n):
        this = [i, (n-i-1)]
        nums.append(this)

    ansOne = -1
    ansTwo = -1
    for _ in range(people):

        # Find stall with maximal min
        maximum = -1
        maxStall = 0
        maxMax = -1
        for i in range(n-1,-1,-1):
            stall = nums[i]
            
            if stall[0] == -1:
                continue
            
            #print(stall, min(stall))
            
            if min(stall) >= maximum:
                if min(stall) == maximum:
                    if max(stall) >= maxMax:
                        maxStall = i
                        maximum = min(stall)
                        maxMax = max(stall)
                else:
                    maxStall = i
                    maximum = min(stall)
                    maxMax = max(stall)

        ansOne = nums[maxStall][0]
        ansTwo = nums[maxStall][1]

        # Occupy stall, update nums
        #print(maxStall)
        #print(nums)


        rightCap = maxStall + nums[maxStall][1] + 1
        leftCap = maxStall - nums[maxStall][0] - 1

        for i in range(leftCap+1, maxStall):
            nums[i][1] -= nums[maxStall][1] + 1

        for i in range(maxStall+1, rightCap):
            nums[i][0] -= nums[maxStall][0] + 1

        nums[maxStall] = [-1,-1]

        #print(nums)
    #print(ansOne, ansTwo)
    return [ansOne, ansTwo]


t = 0
cases = []
f = open("C-small-1-attempt0.in.txt", "r")

for line in f:
    if t == 0:
        t = int(line)
    else:
        data = line.split()
        newCase = []
        newCase.append(int(data[0]))
        newCase.append(int(data[1]))
        cases.append(newCase)

f.close()

out = open("stall.txt", "w")
for i,case in enumerate(cases):
    print(i)
    ret = getLastPerson(case[0], case[1])

    if ret[0] >= ret[1]:
        out.write("Case #" + str(i+1) + ": " + str(ret[0]) + " " + str(ret[1]) + "\n")
    else:
        #out.write()
        out.write("Case #" + str(i+1) + ": " + str(ret[1]) + " " + str(ret[0]) + "\n")


out.close()

'''
for i in range(1,1001):
    print(i)
    getLastPerson(1000,i)


getLastPerson(4,2)
print("-----")
getLastPerson(5,2)
print("-----")
getLastPerson(6,2)
print("-----")
getLastPerson(1000,1000)
print("-----")
getLastPerson(1000,1)
print("-----")
'''
