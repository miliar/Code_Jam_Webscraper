from math import sqrt

INPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C_large_sample.in'
INPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C_first_large_sample.in'
INPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C-small-attempt0.in'
OUTPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C_large_sample.out'
OUTPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C_first_large_sample.out'
OUTPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\C-small-attempt0.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

if 'cache' not in globals():
    cache = {}

def isFair(x):
    length = len(x)
    if 1 == length:
        return True
    for i in range(length / 2):
        if x[i] != x[length-i-1]:
            return False
    return True

def solveQuestion(bottom, top):
    global cache
    print "Solving: %d to %d" % (bottom, top)
    c = 0
    x = bottom
    s = sqrt(x)
    if s != int(s):
        s = int(s)
        x = s ** 2 + (2 * s) + 1
    while x <= top:
        s = sqrt(x)
        if s != int(s):
            # Not a square
            raise Exception("It has to be a square")
        s = int(s)
        #print '%d, %d if square' % (s,x)
        if x in cache:
            if cache[x]:
                c += 1
                print 'Cache hit: %d is fair n square' % x
        else:
            sStr = str(s)
            xStr = str(x)
            if isFair(sStr) and isFair(xStr):
                c += 1
                print '%d is fair n square' % x
                cache[x] = True
            else:
                cache[x] = False
        x += (s * 2) + 1
    return str(c)

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    l = inputFile.readline().split()
    bottom = int(l[0])
    top = int(l[1])
    if top < bottom:
        raise Exception("WTF")
    result = solveQuestion(bottom, top)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
