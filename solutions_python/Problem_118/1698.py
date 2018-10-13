import math

def getFirstPalindrom(number):
    if (number < 10):
        return number
    s = str(number)
    l = len(s)
    s_start, s_middle, s_end = s[:l/2], s[l/2:-(l-1)/2], s[(l-1)/2 + 1:]
    s_rev = s_start[::-1]
    try1 = int(s_start + s_middle + s_rev)
    if (int(s_end) > int(s_rev)):
        return getNextPalindrom(try1)
    return try1

def getNextPalindrom(number):
    s = str(number)
    l = len(s)
    if (l == 1):
        val = s
    else:
        val = s[:-(l-1)/2]
    s_end_rev = str(int(val) + 1)
    s_end = s_end_rev[::-1]
    if (l % 2 == 1):
        s_end_rev = s_end_rev[:-1]
    if (len(s_end) > len(val)):
        s_end = s_end[1:]
    return int(s_end_rev + s_end)

def isPalindrom(number):
    s = str(number)
    l = len(s)
    return s[:l/2] == s[:l/2:-1]

def getSolution(problem):
    start, end = problem
    #we can go the other approach - finding the numbers between the sqrt of start and sqrt of end... (quicker)
    start, end = int(math.ceil(math.sqrt(start))), int(math.floor(math.sqrt(end)))
    #and only going over the palindrom sqrts...
    current = getFirstPalindrom(start)
    count = 0
    while (current <= end):
        if (isPalindrom(current**2)):
            count = count + 1
            #print current
        current = getNextPalindrom(current)
    return str(count)

def readProblem(input_file):
    start, end = [int(x) for x in input_file.readline().split(" ")]
    return (start, end)

def executeFile(file_path):
    input_file = file(file_path, "r")
    output_file = file(file_path + ".out", "w")
    count = int(input_file.readline());
    index = 0
    while (index < count):
        problem = readProblem(input_file)
        sol = getSolution(problem)
        output_file.write("Case #" + str(index + 1) + ": " + sol + "\n")
        index = index + 1
    output_file.close()

def test():
    import time
    def timed(s,e):
        start = time.time()
        sol = getSolution((10**s, 10**e))
        end = time.time()
        t = int(end - start)
        print "[" + str(s) + ":" + str(e) + "]", t, sol
    total = 0
    begining = time.time()
    for i in xrange(14):
        timed(i, i + 1)
        print "\t\t", int(time.time() - begining)
    print "Total: ", int(time.time() - begining)

def test2():
    getSolution((10**0, 10**40))

def main():
    import sys
    if (len(sys.argv) < 2):
        print "Wrong number of arguments!\n" + \
              "Arguments: file_path"
        #test()
        #test2()
        return
    for i in xrange(len(sys.argv) - 1):
        executeFile(sys.argv[i + 1])

if (__name__ == "__main__"):
    main()
