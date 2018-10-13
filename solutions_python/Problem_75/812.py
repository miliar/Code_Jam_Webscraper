filename = "B-large.in"
outputname = filename + "out.txt"

inFile = open(filename, 'r')
outFile = open(outputname, 'w')

numCases = int(inFile.readline())

baseElements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']

for i in range(numCases):
    nextLine = inFile.readline().split()
    counter = 0
    C = int(nextLine[0])
    combos = {}
    for j in range(C):
        combos[nextLine[j+1][0:2]] = nextLine[j+1][2]
        combos[nextLine[j+1][1] + nextLine[j+1][0]] = nextLine[j+1][2]
        
    oppositions = {'Q':'',
                   'W':'',
                   'E':'',
                   'R':'',
                   'A':'',
                   'S':'',
                   'D':'',
                   'F':''}
    D = int(nextLine[C+1])
    for j in range(C+2, C+2+D):
        oppositions[nextLine[j][0]] += nextLine[j][1]
        oppositions[nextLine[j][1]] += nextLine[j][0]

    N = int(nextLine[C+2+D])
    sequence = nextLine[C+3+D]
    result = [sequence[0]]
    for j in range(1, N):
        result += [sequence[j]]
        if len(result) == 1:
            continue
        if result[-1]+result[-2] in combos.keys():
            result = result[0:-2] + [combos[result[-1]+result[-2]]]
        elif oppositions[result[-1]] != '' and result[-1] in baseElements:
            for k in range(len(oppositions[result[-1]])):
                if oppositions[result[-1]][k] in result:
                    result = []
                    break

    outFile.write("Case #" + str(i+1) + ": [")
    for j in range(len(result)-1):
        outFile.write(result[j] + ", ")
    if len(result) > 0:
        outFile.write(result[-1])
    outFile.write("]\n")

inFile.close()
outFile.close()
        
    
        
    
