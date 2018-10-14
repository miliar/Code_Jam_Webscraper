def recycle(n, m):
    nCheck = str(n) + '0'
    i = -2
    while i > -len(nCheck):
        nTemp = nCheck[i:-1] + nCheck[:i]
        if nTemp == str(m):
            return True
        i -= 1
    return False

fileread = open('C-small-attempt0.in', 'r')
filewrite = open('C-small-attempt0-output.txt', 'w')

i = 1
testCases = int(fileread.readline()[:-1]) 
recyclingN = 0

while i <= testCases:
    filereadObj = fileread.readline()
    filereadObj = filereadObj.replace('\n', '')
    filereadObj = filereadObj.split(' ')
    A = int(filereadObj[0])
    B = int(filereadObj[1])
    n = A
    m = n + 1
    while n != B:
        while m != B + 1:
            if recycle(n, m):
                recyclingN += 1
            m += 1
        n += 1
        m = n + 1
    filewrite.write('Case #' + str(i) + ': ' + str(recyclingN) + '\n')
    i += 1
    recyclingN = 0
        
fileread.close()
filewrite.close()
