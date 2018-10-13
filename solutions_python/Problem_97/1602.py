InFile = open("input3.in")
OutFile = open("output3.out","w")
TestCases = int(InFile.readline())
for cases in range(TestCases):
    Line = InFile.readline().split(" ")
    A = int(Line[0])
    B = int(Line[1])
    Pairs = 0
    RecList = []
    for i in range(A,B):
        for j in range(len(str(i))-1,0,-1):
            Rec = int(str(i)[j:] + str(i)[:j])
            if (Rec > i) and (Rec <= B) and ((i,Rec) not in RecList):
                Pairs += 1
                RecList.append((i,Rec))
    OutFile.write("Case #" + str(cases+1) + ": " + str(Pairs)+"\n")
    

InFile.close()
OutFile.close()
