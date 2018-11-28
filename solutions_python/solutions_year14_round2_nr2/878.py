Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T=int(InputList.pop(0))
OutputList = []

for case in range(1,T+1):
    N = int(InputList.pop(0))
    Strings=[]
    for i in range(N):
        Strings.append(InputList.pop(0))
    noMoves = True
    for s in Strings:
        if s != Strings[0]:
            noMoves=False
            break
    if noMoves == True:
        OutputList.append("Case #%d: " %case + str(0) )
    else:
        shortest=0
        shortestLen=len(Strings[0])
        for s in range(len(Strings)):
            if len(Strings[s]) < shortestLen:
                shortestLen=len(Strings[s])
                shortest=s
        targetString = Strings[shortest]
        Moves = 0
        Won = False
        for s in Strings:
            String=s
            c=0
            while String!=targetString:
                if c>=len(String):
                    OutputList.append("Case #%d: Fegla Won" %case)
                    Won = True
                    break
                elif c>=len(targetString):
                    if String[c]==String[c-1]:
                        String = String[:c-1]+String[c:]
                        c-=1
                        Moves+=1
                    else:
                        OutputList.append("Case #%d: Fegla Won" %case)
                        Won = True
                        break
                elif String[c]!=targetString[c]:
                    if c == 0:
                        OutputList.append("Case #%d: Fegla Won" %case)
                        Won = True
                        break
                    elif String[c-1] == targetString[c]:
                        String = String[:c-1]+String[c-1]+String[c-1:]
                        Moves+=1
                    elif String[c]==String[c-1]:
                        String = String[:c-1]+String[c:]
                        c-=1
                        Moves+=1
                    else:
                        OutputList.append("Case #%d: Fegla Won" %case)
                        Won = True
                        break
                c+=1
            if Won:
                break
        if Won == False:
            OutputList.append("Case #%d: " %case + str(Moves))


Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()