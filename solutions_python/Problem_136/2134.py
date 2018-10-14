def calculate(C, F, X):
    time = 0.0
    rps = 2.0
    fRate = C/rps
    xRate = X/rps
    while xRate > fRate + (X/(rps+F)):
        time += fRate
        rps += F
        fRate = C/rps
        xRate = X/rps
    time += xRate
    return "%.7f" % time

def main():
    inFile = "B-large.in"
    #inFile = "input.in"
    outFile = "B-large-output.txt"

    f = open(outFile,'w')
    with open(inFile) as inputFile:
        for i, line in enumerate(inputFile):
            if i > 0:
                case = [float(n) for n in str.split(line)]
                f.write("Case #" + str(i) + ": " + calculate(case[0],case[1],case[2]) + "\n")
    f.close()

if __name__ == '__main__':
    main()