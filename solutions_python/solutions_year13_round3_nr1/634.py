import sys
import numpy as np
from scipy.misc import comb

def InputParser(inputstrs):
    T = int(inputstrs[0])
    residue = inputstrs[1:]
    problems = []
    for i in xrange(T):
        word, N = residue[0].split()
        N = int(N)
        problems.append((word, N))
        residue = residue[1:]

    return problems

vowels = ['a', 'e', 'i', 'o', 'u']

def IsConsonants(character):
    return (not character in vowels)

def Continuity(iclist, N, index, returnlist):
    if iclist.__len__() < N:
        return returnlist
    try:
        ind = iclist[0:N][::-1].index(False)
    except ValueError:
        #returnlist.append(index)  
        length = iclist.__len__()      
        tmpind = N
        additional = 0        
        while(tmpind < length):
            if iclist[tmpind]:
                additional += 1
                tmpind += 1
            else:
                break                        
        returnlist.append((index, additional))
        return Continuity(iclist[tmpind:], N, index + tmpind, returnlist)
    return Continuity(iclist[(N-ind):], N, index + (N-ind), returnlist)

def Nv(length, temp, pre, N):
    index, additional = temp[0], temp[1]
    if not pre == None:         
        pindex, padditional = pre[0], pre[1]
    else:
        pindex = -1
        padditional = 0

    retv = (index  - pindex - padditional) * (length - index - N + 1)         
    for i in range(additional):
        retv += length - index - N -i         
    return retv
    
    
def GetNValue(word, N):
    length = word.__len__()
    iclist = map(IsConsonants, word)
    contlist = Continuity(iclist, N, 0, [])    
    retv = 0    
    if contlist == []:
        return 0
    retv += Nv(length, contlist[0], None, N)
    for i in range(contlist.__len__()-1):
        retv += Nv(length, contlist[i+1], contlist[i], N)
    return retv
    
        
def Solve(problem):
    return GetNValue(problem[0], problem[1])

def OutputString(results):
    outputstrings = []
    for i, result in enumerate(results):
        ostr = 'Case #' + (i+1).__str__() + ': ' + result.__str__()
        outputstrings.append(ostr)

    return outputstrings

if __name__ == '__main__':
    inputfilename = sys.argv[1]      
    
    with open(inputfilename) as f:
        inputstrs = f.readlines()
    
    problems = InputParser(inputstrs)
    results = []
    for i, problem in enumerate(problems):        
        results.append(Solve(problem))
        
    for result in OutputString(results):
        print result