idx = 0

numcases = int(input())

cases = []
d = 0;
for j in range(numcases):
    cases.append(input().split()[1]);

for case in cases:
    d +=1
    numstanding = 0
    numextra = 0
    idx = 0
    for c in case:
        i = int(c)
        if numstanding >= idx:
            numstanding+=i
        elif (idx != 0) and (i != 0):
            numextra += idx - numstanding
            numstanding += numextra
            numstanding+=i
            #print(str(idx) + " : " + str(numstanding) + " : " + str(numextra))
        idx+=1
    print("Case #" + str(d) + ": " + str(numextra))