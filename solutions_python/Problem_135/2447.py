Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T=int(InputList[0])
InputList.pop(0)
Cases = len(InputList)/10
OutputList = []
for case in range(Cases):
    FRow=int(InputList[case*10])-1
    FSquare=[InputList[(case*10)+1], InputList[(case*10)+2], InputList[(case*10)+3], InputList[(case*10)+4]]
    SRow=int(InputList[(case*10)+5])-1
    SSquare=[InputList[(case*10)+6], InputList[(case*10)+7], InputList[(case*10)+8], InputList[(case*10)+9]]
    FStr=FSquare[FRow]
    First=FStr.split()
    SStr=SSquare[SRow]
    Second=SStr.split()
    PossibleNums=[]
    for num in First:
        for num2 in Second:
            if num == num2:
                PossibleNums.append(num)

    if len(PossibleNums) == 1:
        OutputList.append("Case #"+str(case+1)+": "+PossibleNums[0])
    elif len(PossibleNums) == 0:
        OutputList.append("Case #"+str(case+1)+": Volunteer cheated!")
    else:
        OutputList.append("Case #"+str(case+1)+": Bad magician!")

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()