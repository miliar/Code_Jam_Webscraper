def trick(test):
    p1 = int(test[0])
    p2 = int(test[5])
    row1 = set(int(i) for i in str.split(test[p1]))
    row2 = set(int(i) for i in str.split(test[5+p2]))
    result = list(row1&row2)
    if len(result) == 1: return str(result[0])
    elif len(result) > 1: return "Bad magician!"
    else: return "Volunteer cheated!"

def main():
    inFile = "A-small-attempt0.in"
    outFile = "output.txt"

    inputL = []
    with open(inFile) as inputFile:
        for i, line in enumerate(inputFile):
            inputL += [line]
    
    f = open(outFile,'w')
    numOfTest = int(inputL[0])
    for i in range(0, numOfTest):
        f.write("Case #" + str(i+1) + ": " + trick(inputL[1+i*10:1+i*10+10]) + "\n")
    f.close()

if __name__ == '__main__':
    main()