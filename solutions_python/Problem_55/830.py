'''
Created on May 8, 2010

@author: rahul dantkale
'''
def rollerCoaster(fileName):
    fs = open("D:\\GCJ2010\\" + fileName)
    outfs = open("D:\\GCJ2010\\" + fileName + ".out", "w")
    inputData = fs.read().splitlines()
    T = int(inputData[0])
    i = 1
    for t in range(1, len(inputData), 2):
        R, k, N = [int(v) for v in inputData[t].split()] #@UnusedVariable
        r = 0
        groups = [int(g) for g in inputData[t + 1].split()]
        amount = 0
        while r < R:
            r = r + 1
            filled = 0
            groupInRide = []
            while len(groups) > 0 and filled + groups[0] <= k:
                filled = filled + groups[0]
                groupInRide.append(groups.pop(0))
            groups.extend(groupInRide)
            amount = amount + filled
        outfs.write ('Case #{0}: {1}'.format(i, amount))
        outfs.write('\n')
        i = i + 1

rollerCoaster('C-small-attempt0.in')
