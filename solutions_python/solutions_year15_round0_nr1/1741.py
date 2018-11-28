inf = open('i1.txt', 'r')
outf = open('o1.txt', 'w')
lines = list(inf)
inf.close()

cnt = int(lines[0])
for i in range(1, cnt+1):
    splitline = lines[i].split(' ')
    shyness = int(splitline[0])
    audience = []
    for j in range(shyness+1):
        audience.append(int(splitline[1][j]))
    for j in range(len(audience)):
        if audience[j] == 0:
            for k in range(j-1, -1, -1):
                if audience[k] > 1:
                    audience[k] -= 1
                    audience[j] = 1
                    break
    ans = audience.count(0)
    outf.write("Case #" + str(i) + ": " + str(ans) + "\n")

outf.close()
