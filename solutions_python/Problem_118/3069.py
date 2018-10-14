import math

ends = [1, 4, 5, 6, 9]
sqrts = {}
results = 0
case = 0


def endCheck(number):
    return (number % 10) in ends


def palCheck(number):
    word = str(number)
    return word == word[::-1]


def makeSquares(a, b):
    #sqrts = {}
    for i in range(a, b+1):
        #if endCheck(i):
        sqrts[i*i] = i
    print sqrts
    return True


def checkNums(aa, bb):
    global case, sqrts, results
    for ii in range(aa, bb+1):
        if endCheck(ii):
            if palCheck(ii):
                if ii in sqrts:
                    i = sqrts[ii]
                    print 'testing', str(ii), str(i)
                    if palCheck(i):
                        print 'found ' + str(ii)
                        results += 1

lines = ''
def test(aa, bb):
    global case, sqrts, results, lines
    a = int( math.sqrt(aa) )
    b = int( math.ceil( math.sqrt(bb) ) )
    #print 'makin squares', str(case), 'from', str(a), 'to', str(b)
    makeSquares(a, b)
    checkNums(aa, bb)
    lines += 'Case #'+str(case)+': '+ str(results) +'\n'
    print 'Case#' + str(case) + ': ' + str(results)


filename = 'C-small-attempt1.in'
f = open(filename, 'r')
numtests = int(f.readline())  # readline() reads the next line as a string.
o = open('output1.txt', 'w+')  # (create if doesn't exist and) open output file in write mode

testcount = 0
while testcount < numtests:
    global case, sqrts, results, lines
    case += 1
    results = 0
    bounds = f.readline().split()
    aa = int(bounds[0])
    bb = int(bounds[1])
    #print 'testing case', str(case), 'from', str(aa), 'to', str(bb)
    test(aa, bb)
    testcount += 1
    if testcount >= numtests:
        o.write(lines)