from sys import stdin

i = 0
fw = open("output.txt", "w")
with open("A-large.in") as f:
    numberOfTests = f.readline()
    for line in f:
        if i < numberOfTests:
            maxSi = int(line.split(" ")[0])
            count = 0
            countNeeded = 0
            j = 0
            for numberIn in list(line.split(" ")[1].rstrip()):
                if count < j and j <= maxSi:
                    countNeeded += 1
                    count += 1
                count += int(numberIn)
                j += 1
            fw.write("Case #" + str(i + 1) + ": " + str(countNeeded) + "\n")
        else:
            break;
        i += 1
fw.close()
