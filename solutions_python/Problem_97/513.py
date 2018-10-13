inputFile = open("C-large (1).in", 'r')
outputFile = open("recycleOutLarge.txt", 'w')
numTests = int(inputFile.readline())

def countRecycle(a,b):
    count = 0
    for n in range(a,b):
        nStr = str(n)
        ms = {}
        for k in range(1, len(nStr)):
            m = int(nStr[k:] + nStr[0:k])
            if m in ms:
                continue
            if m > n and m <= b:
                ms[m] = 1
                count += 1
    return count

def countRecycle2(a,b):
    count = 0
    for n in range(a, b-1):
        for m in range(n+1,b):
            nStr = str(n)
            canRecycle = False
            for k in range(len(nStr)):
                if nStr[k:] + nStr[0:k] == str(m):
                    canRecycle = True
                    break
            if canRecycle:
                count += 1
    return count


for i in range(numTests):
    line = inputFile.readline().split()
    a = int(line[0])
    b = int(line[1])
    outputFile.write('Case #' + str(i+1) + ': ' + str(countRecycle(a,b)) + '\n')


inputFile.close()
outputFile.close()
