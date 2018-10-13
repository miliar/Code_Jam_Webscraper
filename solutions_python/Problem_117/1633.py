import os

class Lawn(object):
    def __init__(self, N, M):
        self.grass = []
        self.N = N
        self.M = M

    def appendRow(self, str):
        arr = []
        for i in str.split(" "):
            arr.append(int(i))
        self.grass.append(arr)

    def checkIfPossible(self, n, m):
        curr = self.grass[n][m]
        if (curr == 2):
            return True
        else:
            # check going up
            found = True
            for i in xrange(n, -1, -1):
                if self.grass[i][m] == 2:
                    found =  False
                    break
            # check going down
            for i in xrange(n, self.N):
                if self.grass[i][m] == 2:
                    found =  False
                    break
            if (found): return True
            found = True
            # check going left
            for i in xrange(m, -1, -1):
                if self.grass[n][i] == 2:
                    found = False
                    break
            # check going right
            for i in xrange(m, self.M):
                if self.grass[n][i] == 2:
                    found = False
            if (found): return True

        return False


input_file = open(os.getcwd() + "/B.in", 'r')

T = input_file.readline()

for i in xrange(0, int(T)):
    print "Case #%d:" % (i+1),
    dimensions = input_file.readline().split(" ")
    myLawn = Lawn(int(dimensions[0]), int(dimensions[1]))
    for j in xrange(0, int(dimensions[0])):
        myLawn.appendRow(input_file.readline())
    lawn_is_good = True
    for n in xrange(0, int(dimensions[0])):
        for m in xrange(0, int(dimensions[1])):
            if (not myLawn.checkIfPossible(n, m)):
                lawn_is_good = False
                break
        if not lawn_is_good:
            break
    if lawn_is_good:
        print "YES"
    else:
        print "NO"