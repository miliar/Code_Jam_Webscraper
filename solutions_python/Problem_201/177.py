from __future__ import print_function

def solveProblem(N, K):
    while not K == 1:
        if (N % 2) == 0:
            if(K % 2) == 0:
                N = N/2
                K = K/2
            else:
                N = N/2 - 1
                K = (K - 1) / 2
        else:
            N = (N - 1) / 2
            if(K % 2) == 0:
                K = K/2
            else:
                K = (K - 1) / 2
    if (N % 2) == 0:
        ls = N/2 - 1
        rs = N/2
    else:
        ls = (N - 1)/2
        rs = (N - 1)/2
    return [max([ls, rs]), min([ls, rs])]

import sys

def main():
    inPath = sys.argv[1]
    outPath = inPath.split('.')[0] + '.out'
    file = open(inPath, "r")
    out = open(outPath, "w")
    case = 0
    #Read Input File
    for line in file:
        #Skip first line
        if case == 0:
            case += 1
            continue
        #solve problem
        inputs = line.split(' ')
        result = solveProblem(int(inputs[0]), int(inputs[1]))
        #format Problem
        resultStr = ""
        for r in result:
            resultStr += str(r) + ' '
        print('Case #{case}: {resultStr}'.format(case=case, resultStr=resultStr), file=out)
        case += 1

if __name__ == "__main__":
    main()