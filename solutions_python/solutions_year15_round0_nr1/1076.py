inFile = open('A-large.in', 'r')
outFile = open('b.txt', 'w')
lines = []

for i in inFile:
    i.strip()
    lines.append(list(map(str, i.split(' '))))
    
sing = int(lines[0][0])
rest = lines[1:]

def tc(a, strx):
    ppl = 0
    inv = 0
    for i in range(a+1):
        if ppl < i:
            inv += i - ppl
            ppl = i

        ppl += int(strx[i])
    return inv

for i in range(sing-1):
    a, b = int(rest[i][0]), rest[i][1].strip()

    outFile.write("Case #"+str(i+1)+': ' + str(tc(a, str(b))))
    outFile.write("\n")
i+=1
a, b = int(rest[i][0]), rest[i][1].strip()

outFile.write("Case #"+str(i+1)+': ' + str(tc(a, str(b))))
inFile.close()
outFile.close()
