def isTidy(num):
    sNum = str(num)
    tidy = ''.join(sorted(sNum))
    return sNum == tidy

fOut = open('B-small-attempt0.out', 'w')

with open('B-small-attempt0.in') as fin:
    num = int(fin.readline().strip())  # number of test cases

    for i in range(0, num):
        N = int(fin.readline().strip())
        found = isTidy(N)
        while not found:
            N -= 1
            found = isTidy(N)

        fOut.write('Case #%i: %i\n' % (i+1, N))

fOut.close()