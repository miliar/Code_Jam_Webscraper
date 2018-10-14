readFile = open("A-large.in", "r")
writeFile = open("Abigoutput", "w")
num_inputs = int(readFile.readline().strip())
for case in range(num_inputs):
    string, flipperSize = readFile.readline().split()
    lenString = len(string)
    flipperSize = int(flipperSize)
    string = list(string)
    minFlips = 0
    for i in range(lenString - flipperSize + 1):
        if string[i] == "-":
            minFlips += 1
            for j in range(flipperSize):
                if string[i+j] == "+":
                    string[i+j] = "-"
                elif string[i+j] == "-":
                    string[i+j] = "+"
    if "-" in string:
        writeFile.write("Case #" + str(case+1) + ": IMPOSSIBLE\n")
    else:
        writeFile.write("Case #" + str(case+1) + ": " + str(minFlips) + "\n")