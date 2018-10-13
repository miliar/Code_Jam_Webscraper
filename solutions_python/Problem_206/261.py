#python 2.7

import sys
import math
import string
import itertools        

def calcHorseCompleteTime(D, k, s):
    delta = D - k
    return float(delta)/s

def solve(D, K, S):
    maxCompleteTime = 0 
    for i in range(len(K)):
        completeTime = calcHorseCompleteTime(D,K[i],S[i])
        maxCompleteTime = max(completeTime, maxCompleteTime)
        print maxCompleteTime
    return str(D/float(maxCompleteTime))

    
def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    idx = 1
    case = 1
    while True:
        #print split_input[idx]
        D, N = [int(x) for x in split_input[idx].split(' ')]
        idx += 1
        K = list()
        S = list()
        for i in range(0,N):
            k, s = [int(x) for x in split_input[idx].split(' ')]
            K.append(k)
            S.append(s)
            idx += 1
        print "Input, Case #" + str(case) + ": " + str([D, N, K, S])
        res= solve(D, K, S)
        print "Result, Case #" + str(case) + ": " + str(res)
        output_file.write("Case #" + str(case) + ": " + str(res) + "\n")
        case += 1
        if (case > case_count):
            break
        
    
if __name__ == "__main__":
    main()
