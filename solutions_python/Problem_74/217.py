cin = open("in.txt")
cout = open("out.txt" , "w")
TestCase = cin.readline()
for CaseNumber in range(1 , int(TestCase) + 1):
    TimeOrange , PosOrange = 0 , 1
    TimeBlue , PosBlue = 0 , 1
    N = cin.readline().split()
    for i in range(0 , int(N[0])):
        who = N[2 * i + 1]
        pos = int(N[2 * i + 2])
        if who == "O":
            TimeOrange = max(TimeOrange + abs(pos - PosOrange) + 1 , TimeBlue + 1)
            PosOrange = pos
        else:
            TimeBlue = max(TimeBlue + abs(pos - PosBlue) + 1 , TimeOrange + 1)
            PosBlue = pos
    cout.write("Case #" + str(CaseNumber) + ": " + str(max(TimeOrange , TimeBlue)) + "\n")
