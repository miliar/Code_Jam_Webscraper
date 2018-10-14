fin = open("a.in", "r")
fout = open("a.out", "w")
lines = fin.readlines();

caseMax = int(lines[0]);
caseCount = 1;

for caseCount in range(1, caseMax+1):
    A, B = map(int, lines[caseCount * 2 - 1].split())
    possibilities = map(float, lines[caseCount * 2].split())

    expectedMin = B * 3 + 2

    for back in range(A+1):
        correctStroke = 2 * back + B - A + 1
        wrongStroke = 2 * back + B - A + B + 2
        expected = 0

        for caseFlag in range(2**A):
            combinePossibility = 1
            for i in range(A):
                combinePossibility = combinePossibility * ((1-possibilities[A-i-1]) if (2**i & caseFlag) else possibilities[A-i-1])
            expected = expected + combinePossibility * (correctStroke if (2**back > caseFlag) else wrongStroke)
    
        if expectedMin > expected:
            expectedMin = expected

    # enter now
    if expectedMin > B + 2:
        expectedMin = B + 2

    fout.write("Case #%d: %.6f\n" % (caseCount, expectedMin))

fin.close()
fout.close()

print 'Done!'
