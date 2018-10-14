if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    inFile = open(fname, 'r')
    numCases = int(inFile.readline())
    for case in xrange(numCases):
        # Get the number range
        a,b = map(int, inFile.readline().split())

        # Get the potential numbers
        allNums = map(str, range(a, b + 1))

        # Store pairs
        nums = set()
        for n in allNums:
            nInt = int(n)
            for ind in range(len(n)):
                newNum = int(n[ind:] + n[:ind])
                #print ind, nInt, newNum, n[ind]
                if a < newNum < b and nInt != newNum and n[ind] != 0:
                    nums.add((min(nInt, newNum), max(nInt, newNum)))

        print 'Case #%d: %s' % (case + 1, len(nums))
    inFile.close()
