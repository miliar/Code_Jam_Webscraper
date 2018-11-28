inFile = open("D-small-attempt0.in", 'r')
outFile = open('a1.txt', 'w')
lines = []
maj = 0
for i in inFile:
    i=i.strip()
    if len(str(i)) == 1 or len(str(i)) == 2:
        maj = int(i)
    else:
        a, b, c = list(map(int, i.split(' ')))
    
        lines.append([a, b, c])
def solv03d(a, b, c):
    if a == 1:
        return "GABRIEL"
    elif a == 2:
        if (b*c)%2==0:
            return "GABRIEL"
        else:
            return "RICHARD"
    elif a == 3:
        x=[b, c]
        x.sort()
        if x == [2, 3] or x == [3, 4] or x == [3, 3]:
            return "GABRIEL"
        else:
            return "RICHARD"
    else:
        x=[b, c]
        x.sort()
        if x == [3, 4] or x == [4, 4]:
            return "GABRIEL"
        else:
            return "RICHARD"

for i in range(maj-1):
    a, b, c = lines[i][0], lines[i][1], lines[i][2]
    outFile.write("Case #"+str(i+1)+": "+solv03d(a, b, c))
    outFile.write("\n")

i+=1
a, b, c = lines[i][0], lines[i][1], lines[i][2]
outFile.write("Case #"+str(i+1)+": "+solv03d(a, b, c))
inFile.close()
outFile.close()
