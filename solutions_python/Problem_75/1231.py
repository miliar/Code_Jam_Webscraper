'''
Created on May 7, 2011

@author: b44nz0r
'''

h = open(r'X:\Desktop\B-small.in')
out = open(r'X:\Desktop\answer.txt','w')
numCases = h.readline()

def isPresent(alpha,dict):
    if alpha in dict.keys():
        return dict[alpha]
    else:
        return None

for i in range(0,int(numCases)):
    final = []
    merging = {}
    conflictingPairs = {}
    line = h.readline()
    segs = line.rstrip().split(' ')
    numMerge = int(segs[0])
    numConflict = int(segs[numMerge+1])
    stringLen = int(segs[numMerge+numConflict+2])
    str = segs[numMerge+numConflict+3]
    for j in range(0,numMerge):
        merge = segs[j+1]
        merging[merge[0:2]] = merge[2]
        merging[merge[1]+merge[0]] = merge[2]
    
    for k in range(numMerge+2,numMerge+2+numConflict):
        conflictingPairs[segs[k][0]] = segs[k][1]
        conflictingPairs[segs[k][1]] = segs[k][0]
        
    for l in range(0,stringLen):
        if len(final) == 0:
            final.append(str[l])
        else:
            mergeChar = isPresent(final[len(final)-1]+str[l], merging) 
            if mergeChar != None:
                final.pop()
                conflictChar = isPresent(mergeChar, conflictingPairs)
                if conflictChar != None:
                    if conflictChar in final:
                        final = []
                    else:
                        final.append(mergeChar)
                else:
                    final.append(mergeChar)
            else:
                conflictChar = isPresent(str[l], conflictingPairs)
                if conflictChar != None:
                    if conflictChar in final:
                        final = []
                    else:
                        final.append(str[l])
                else:
                    final.append(str[l])
#    print final
        
    out.write('Case #%d: ['%(i+1))
    for a in range(0,len(final)):
        if a == len(final)-1:
            out.write(final[a])
        else:
            out.write(final[a]+', ')
    out.write(']\n')

h.close()
out.close()