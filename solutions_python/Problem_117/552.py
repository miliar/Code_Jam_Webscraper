def checkRow(arr, i, val):
    for v in arr[i]:
        if v > val:
            return True

    return False

def checkCol(arr, j, val):
    for i in xrange(len(arr)):
        if arr[i][j] > val:
            return True

    return False

def canMaw(arr, N, M):
    for i in xrange(N):
        for j in xrange(M):
            if checkRow(arr, i, arr[i][j]) and checkCol(arr, j, arr[i][j]):
                return "NO"

    return "YES"


f = open('1-small-practice.in.txt', 'r')
fw = open('1-small-out.txt', 'w')

for i in xrange(int(f.readline())):
    N, M = [int(j) for j in f.readline().split()]
    arr = []
    for x in xrange(N):
        arr.append([int(j) for j in f.readline().split()])

    fw.write('Case #' + str(i+1) + ': ' + canMaw(arr, N, M) + '\n')

fw.close()
f.close()
