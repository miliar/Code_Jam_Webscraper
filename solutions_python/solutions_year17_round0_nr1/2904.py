def __main__():
    f = open("in.txt", 'r')
    o = open("out.txt", 'w')
    noOfCases = int(f.readline())
    for testNo in range(noOfCases):
        line = f.readline()
        line = line.split()
        cakes = list(line[0])
        fLen = int(line[1])
        out = ""
        counter = 0
        for i in range(len(cakes)):
            if cakes[i] == '-':
                if i <= len(cakes) - fLen:
                    counter += 1
                    for j in range(i, i + fLen):
                        if cakes[j] == '-':
                            cakes[j] = '+'
                        else:
                            cakes[j] = '-'
                else:
                    counter = "IMPOSSIBLE"
                    break
        o.write("Case #" + str(testNo + 1) + ": " + str(counter) + "\n")
    f.close()
if __name__ == '__main__':
    __main__()
