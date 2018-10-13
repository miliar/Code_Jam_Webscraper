Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T=InputList[0]
OutputList = []
Count = 1
for case in range(int(T)):
    N = int(InputList[Count].split()[0])
    M = int(InputList[Count].split()[1])
    if N == 1:
        OutputList.append("Case #" + str(case+1) + ": YES")
    elif M == 1:
        OutputList.append("Case #" + str(case+1) + ": YES")
    else:
        lawn=[]
        for row in range(N):
            lawn.append(InputList[Count+1+row])
        No = False
        for rw in lawn:
            if "1" in rw:
                if "2" in rw:
                    count = 0
                    for height in rw:
                        if height == "1":
                            for i in range(N):
                                if lawn[i][count]=="2":
                                    OutputList.append("Case #" + str(case+1) + ": NO")
                                    No = True
                                    break
                        count += 1
                        if No:
                            break
            if No:
                break
        if No == False:
            OutputList.append("Case #" + str(case+1) + ": YES")
    Count += N+1

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()