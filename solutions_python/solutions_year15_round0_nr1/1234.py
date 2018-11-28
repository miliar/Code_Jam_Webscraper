#inputFile = r"A-small-attempt0.in"
#inputFile = r"Example.in"
inputFile = r"A-large.in"
outputFile = inputFile.replace("in", "out")    

def solve(line):
    s = line.split()
    Smax = s[0]
    people = [int(x) for x in s[1]]
    return str(addShyPeople(people))
    
def addShyPeople(people):
    standing = 0
    toAddPeople = 0
    for i, p in enumerate(people):
        while(standing < i):
            toAddPeople += 1
            standing += 1
            
        standing += p
    return toAddPeople

if __name__ == '__main__':
    lines = open(inputFile, 'r').read().split('\n')
    
    cases = int(lines[0])
    with open(outputFile, 'w') as f:
        for case in range(0,cases):
            print(case)
            startIndex = case  + 1
            solution = solve(lines[startIndex])
            caseSolution = "Case #" + str(case + 1) + ": " + solution
            print(caseSolution)
            print(caseSolution, file=f)
        