def readFile(inFile, outFile):
    with open(inFile) as f:
        line1 = f.readline()
        #print("Number of Cases: ", line1)
        counter = 1
        for line in f:
            line = line.strip()
            calculateSolution(line, counter, outFile)
            counter += 1

def calculateSolution(line, counter, outFile):
    h = line.split()
    pancakes = h[0]
    flipper = int(h[1])
    solution = doSolve(pancakes, flipper)
    #print(line)
    #print("Solution : " + str(solution) + "\n")
    with open(outFile, 'a') as f:
        f.write("Case #%i: %s\n"  %(counter,solution))
    
def doSolve(pancakes, flipper):
    counter = 0
    while True:
        index = pancakes.find('-')
        if index == -1:
            return counter
        if index+int(flipper) > len(pancakes):
            return "IMPOSSIBLE"
        pancakes = flip(pancakes, index, flipper)
        counter += 1
        #ret = doSolve(pancakes, flipper)
        #if ret == "IMPOSSIBLE":
        #    return ret
        #else:
        #    return ret+1
    
def flip(pancakes, index, flipper):
    pan = list(pancakes)
    for i in range(index, index+flipper):
        if pan[i] == '+':
            pan[i] = '-'
        else:
            pan[i] = '+'
    return "".join(pan)

readFile("A-large.in", "A-large.out")
