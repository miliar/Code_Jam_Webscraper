import numpy as np
import pandas as pd

def readInputFile(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content

def convertToBin(seq):
    seq = str(seq).replace('+','1')
    seq = str(seq).replace('-','0')
    return seq

def countFlips(seq,K):
    binseq = convertToBin(seq)    
    intseq = int(K*'1')
    flips = 0
    for i in np.arange(0,len(seq)-K+1):        
        if binseq[i]=='0':
            #print(binseq[0:i]+str(abs(int(binseq[i:(i+K)])-intseq))+binseq[(i+K):])
            binseq = binseq[0:i]+str(abs(int(binseq[i:(i+K)])-intseq))+binseq[(i+K):]
            flips += 1
    if ('0' in binseq):
        return 'IMPOSSIBLE'
    else:
        return flips
    
def solveA(fnamein,fnameout):
    inputlist = readInputFile(fnamein)
    outputarr = list()
    T = int(inputlist[0])
    for i in np.arange(1,T+1):
        temp_input = inputlist[i].split(' ')
        seq,K = temp_input[0], int(temp_input[1])
        flips = countFlips(seq,K) 
        outputarr.append('Case #'+str(i)+': '+str(flips))
        
    # Write to file
    with open(fnameout, "w") as output:
        for item in outputarr:
            output.write("%s\n" % item)
            
solveA('A-large.in','A-large-output.txt')