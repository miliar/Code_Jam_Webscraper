fname = 'B-small-attempt0.in'
with open(fname) as f:
    Data = f.read().splitlines()
data = []
for i in Data:
    data.append([float(j) for j in i.split()]) if len(i.split()) > 1 else data.append(int(i))
NumCases = data[0]
del data[0]
Cases = data
CC = 1
while Cases:
    MinimumTime = None
    Case = Cases.pop(0)
    CRate = 2.0
    C,F,X = Case[0],Case[1],Case[2]
    TTaken = []
    if C/CRate + X/(CRate + F) < X/CRate:
        MinimumTime = C/CRate + X/(CRate+F)
        TTaken.append(C/CRate)
        CRate += F
        while sum(TTaken) + C/CRate + X/(CRate+F) < MinimumTime:
            MinimumTime = sum(TTaken) + C/CRate + X/(CRate+F)
            TTaken.append(C/CRate)
            CRate += F
        print "Case #" + str(CC) + ": " + str(round(sum(TTaken) + X/CRate,7))
    else:
        print "Case #" + str(CC) + ": " + str(round(X/CRate,7))
    CC += 1