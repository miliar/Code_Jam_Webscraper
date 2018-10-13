Data = open("input.in", "r")
Out = open("output.txt", "w")

def isOkay(Shyness):
    Stood = Shyness[0]
    for t in range (1, len(Shyness)):
        if Stood < t: return 0
        Stood += Shyness[t]
    return 1

T = int(Data.readline())

for i in range(T):
    S, string = Data.readline().split()
    Shy = [int(j) for j in string]
    Extra = 0
    while isOkay(Shy) == 0:
        Extra += 1
        Shy[0] += 1
    Out.write("Case #" + str(i + 1) + ": " + str
(Extra) + "\n")

Data.close()
Out.close()
