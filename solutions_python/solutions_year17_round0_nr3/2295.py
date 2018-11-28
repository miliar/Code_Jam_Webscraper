import numpy as np
import pandas as pd

def findBinSplit(S):
    binarylength = len(bin(S))-2
    split = 2**binarylength
    return split

def findMinMax(N,S):
    split = findBinSplit(S)
    minNeighbor = np.floor(float(N-S)/split)
    maxNeighbor = round(float(N-S)/split)
    return [int(maxNeighbor),int(minNeighbor)]

def readInputFile(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content

def solveC(fnamein,fnameout):
    inputlist = readInputFile(fnamein)
    outputarr = list()
    T = int(inputlist[0])
    for i in np.arange(1,T+1):
        temp_input = inputlist[i].split(' ')
        N,S = int(temp_input[0]), int(temp_input[1])
        minmax = findMinMax(N,S) 
        outputarr.append('Case #'+str(i)+': '+str(minmax[0])+' '+str(minmax[1]))
        
    # Write to file
    with open(fnameout, "w") as output:
        for item in outputarr:
            output.write("%s\n" % item)

solveC('C-small-2-attempt0.in','C-small-2-output.txt')