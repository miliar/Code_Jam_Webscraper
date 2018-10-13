import argparse
import re

COOK_PER_SEC = 2
MIN_DIFF = 0.0000001

def findMinTime(C,F,X):
    totTime = X / COOK_PER_SEC
    n = 1
    newTime, prevSum = findTime(C,F,X,n)
    while (totTime > newTime) and (abs(totTime - newTime) > MIN_DIFF):
        totTime = newTime
        n += 1
        newTime, prevSum = findTime(C,F,X,n,prevSum)

    return totTime

def findTime(C,F,X,n,prevSum=0):
    if prevSum != 0:
        sumUp = prevSum + (C/(COOK_PER_SEC + (n-1)*F))
    else:  
        sumUp = C/(COOK_PER_SEC)
    return (X/(COOK_PER_SEC + n*F) + sumUp), sumUp

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', nargs = 1, metavar = 'INPUT', help = "Input file", required = True, dest = 'input_file')
    return parser.parse_args()    


if __name__ == "__main__" :

    args = args()

    if args.input_file[0] is not None:
        input_file = args.input_file[0]
    else:
        logger.error('Error: no input_file.')
        sys.exit(-1)

    output = ''

    with open(input_file, 'r') as f:
        lines = f.readlines()
        numTest = int(lines[0].strip())
        i = 0
        while i < numTest:
            values = map(float, 
                re.findall(r'^(\d+\.\d{1,5})\s(\d+.\d{1,5})\s(\d+.\d{1,5})', 
                    lines[i+1])[0])
            X = values.pop()
            F = values.pop()
            C = values.pop()
            expRes = findMinTime(C, F, X)
            output += 'Case #' + str(i+1) + ': ' + "{0:.7f}".format(expRes)
            if numTest != i+1:
                output += '\n'
            i += 1

    print output

    with open('output2.txt', 'w') as f:
        f.write(output)
    