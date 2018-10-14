'''
Created on May 4, 2013

@author: user
'''
import sys
import bisect

def countChanges(size, others):
    others = sorted(others)
    nMotes = len(others)
    changes = 0
    # others[k] < size for k < maxIdx
    maxIdx = 0
    
    while maxIdx < nMotes:
        lastConsumedIdx = maxIdx
        maxIdx = bisect.bisect_left(others, size, lo=lastConsumedIdx)

        if lastConsumedIdx == maxIdx:
            # stuck for now, either keep consuming or remove
            # see which is more efficient
            
            nextSize = others[lastConsumedIdx]
            nRemaining = nMotes - lastConsumedIdx
            tempChanges = 0

            if size <= 1:
                # cannot add smaller, just remove
                changes += nRemaining
                break;
            else:
                while size <= nextSize:
                    # try adding and consuming maximal motes
                    size += size - 1
                    tempChanges += 1
                            
                if tempChanges >= nRemaining:
                    # more efficient to remove
                    changes += nRemaining
                    break;
                else:
                    # adding a mote works, so confirm changes for maximal mote
                    changes += tempChanges
                    maxIdx = bisect.bisect_left(others, size, lo=lastConsumedIdx)

        # absorb smaller motes
        size += sum(others[lastConsumedIdx: maxIdx])

    return changes
    

def processFile(fileName):
    results = []
    with open(fileName) as handle:
        trials = int(handle.readline().strip())
        for i in range(trials):
            size0, motes = [int(x) for x in handle.readline().strip().split(" ")]
            others = [int(x) for x in handle.readline().strip().split(" ")]
            results.append(countChanges(size0, others))     
    return results
   
   
def writeResults(results, fileName):
    with open(fileName, 'w') as handle:
        case = 1
        for result in results:
            handle.write('Case #{}: {}\n'.format(case, result))
            case += 1
            

def main():
    results = processFile(sys.argv[1])
    writeResults(results, sys.argv[2])

if __name__ == '__main__':
    main()