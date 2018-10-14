'''
Created on May 4, 2013

@author: Allen
'''
import os

def osmos(data):
    mote, motes = data[0], data[1]
    #if mote == 1: # all motes must be removed
    #    return len(motes)
    
    # exhaustive search
    array = [] # indexed by addMax, removeMax containing mote, motes array
    array.append([expand(mote, motes)]);
    upperBound = len(array[0][0][1])
    if(upperBound == 0):
        return 0
    
    for currOp in range(1, upperBound):
        for removeMax in range(currOp):
            addMax = currOp - removeMax

            if removeMax == 0:
                ref = array[addMax - 1][0]
                array.append([expand(ref[0] * 2 - 1, ref[1])])
            else:
                ref = array[addMax][removeMax - 1]
                array[addMax].append([ref[0], ref[1][:-1]])
            
            if(len(array[addMax][removeMax][1]) == 0):
                return currOp
    
    return upperBound

# returns an equivalent array where the mote has absorbed all motes possible
def expand(mote, motes):
    maxSize = mote
    unreachable = []
    
    for index, mote in enumerate(motes):
        if(mote < maxSize):
            maxSize += mote
        else:
            unreachable = motes[index:]
            break

    return maxSize, unreachable

if __name__=="__main__":
    name = 'A-large'
    cases = []
    with open(os.path.join(os.path.dirname(__file__), name + '.in')) as f:
        T = int(f.readline())
        for dummy in range(T):
            dim = [int(i) for i in f.readline().split()]
            curr = []
            curr.append(dim[0])
            curr.append(sorted([int(i) for i in f.readline().split()]))
            cases.append(curr)
    
    output = ""
    for i in range(T):
        output += "Case #{0}: {1}\n".format(i+1, osmos(cases[i]))
    
    with open(os.path.join(os.path.dirname(__file__), name + '.out'), 'w') as f:
        f.write(output[:-1])