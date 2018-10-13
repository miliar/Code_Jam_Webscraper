 
def readFile(inFile,outFile):
    with open(inFile) as f:
        line1 = f.readline()
        #print("Number of Cases: ", line1)
        counter = 1
        for line in f:
            line = line.strip()
            calculateSolution(line, counter, outFile)
            counter += 1
            
def calculateSolution(line, counter, outFile):
    found = False
    while True:
        newLine = betterCheck(line)
        if line == newLine:
            line = str(int(line))
            break
        line = newLine
    with open(outFile, 'a') as f:
        f.write("Case #%i: %s\n"  %(counter,line))
        
def solve(line, i):
    if i == 0:
        part1 = ""
    else:
        part1 = line[:i-1]
    part2 = str(int(line[i-1])-1)
    if len(line) == i:
        part3 = ""
    else:
        part3 = '9' * (len(line)-i)
    return part1+part2+part3

def betterCheck(line):
    digit = 0
    for i in range(len(line)):
        if digit > int(line[i]):
            line = solve(line, i)
            return line
        digit = int(line[i])
    return line
    
    
readFile("B-large.in", "B-large.out")
