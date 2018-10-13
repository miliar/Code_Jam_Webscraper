fin = open("A-large.in", "r")
fout = open("output.txt", "w")

tc = int(fin.readline())
for t in range(0, tc):
    temp = fin.readline().split()
    cakes = temp[0]
    k = int(temp[1])
    result = 0
    for i in range(0, len(cakes)-k+1):
        if cakes[i] == '-':
            result = result + 1
            for j in range(i, i+k):
                if cakes[j] == '-':
                    cakes = cakes[:j] + '+' + cakes[j+1:]
                    #cakes[j] = '+'
                else:
                    cakes = cakes[:j] + '-' + cakes[j+1:]
                    #cakes[j] = '-'
    
    isOk = True
    for ch in cakes:
        if ch == '-':
            fout.write("Case #" + str(t+1) + ": IMPOSSIBLE\n")
            isOk = False
            break
    if isOk:
        fout.write("Case #" + str(t+1) + ": " + str(result) + "\n")

fin.close()
fout.close()