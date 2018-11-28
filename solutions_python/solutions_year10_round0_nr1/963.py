'''
Created on May 8, 2010

@author: rahul dantkale
'''
def snapping (fileName):
    fs = open("D:\\GCJ2010\\" + fileName)
    outfs = open("D:\\GCJ2010\\" + fileName + ".out", "w")
    inputData = fs.read().splitlines()
    for i in range(1, len(inputData)):
        N, K = inputData[i].split()
        snappers = [0 for s in range(int(N))]
        for snap in range(int(K)):
            if snappers[0] == 0:
                snappers[0] = 1
            elif snappers[0] == 1:
                for j in range(int(N)):
                    if snappers[j] == 1:
                        snappers[j] = 0
                    else:
                        snappers[j] = 1
                        break
        result = "OFF"
        value = snappers[0]
        for k in range(1, int(N)):
            if value == 0: break
            value = value & snappers[k]           
        if value == 1: result = "ON"
        outfs.write('Case #{0}: {1}'.format(i, result))
        outfs.write('\n')

snapping("A-small-attempt3.in")
