"""
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest,
her pencils are sorted from shortest to longest and her computers from oldest to newest.

One day, when practicing her counting skills, she noticed that some integers, when written
in base 10 with no leading zeroes, have their digits sorted in non-decreasing order.
Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy.
Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N.
What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow.
Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number
(starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 <= T <= 100.
Small dataset

1 <= N <= 1000.
Large dataset

1 <= N <= 10^18.

Input
4
132
1000
7
111111111111111110

Output
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999


"""

input_file_name = 'B-large.in'
output_file_name = 'B-large.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

def naive(N):
    print 'N: {}'.format(N)

    found = False
    n = long(N)

    if n > 100000:
        diff = n - 99999999999999999
        print 'diff: {}'.format(diff)
        return None

    while(not found):
        print 'n: {}'.format(n)
        if isTidy(str(n)):
            # print '{} is tidy'.format(n)
            output = 'Case #{}: {}'.format((t+1), n)
            print output
            outFile.write(output + "\n")
            found = True
        n-=1

def isTidy(n):
    numDigits = len(n)

    sameCount = n.count(n[0])
    # print 'sameCount: {}'.format(sameCount)

    if sameCount == numDigits:
        return True

    lastDigit = int(n[numDigits-1])

    for idx in range(numDigits-2, -1, -1):
        # print 'idx: {}'.format(idx)
        digit = int(n[idx])
        # print 'comparing {} with {}'.format(current, digit)
        if digit > lastDigit:
            return False
        lastDigit = digit

    return True

def getTidy(n):
    numDigits = len(n)

    current = int(n[0])
    idx = 1
    nonTidyIndex = 0
    while (idx < numDigits):
        nextDigit = int(n[idx])
        # print 'comparing {} with {}'.format(current, nextDigit)
        if nextDigit < current:
            # print 'not tidy at index {}'.format(idx)
            nonTidyIndex = idx
            break
        current = nextDigit
        idx+=1

    # go one index less than the nonTidyIndex, reduce the digit at that index
    nonTidyIndex-=1
    digits = list(n)
    # print 'digits: {}'.format(digits)
    digit = n[nonTidyIndex]
    value = int(digit)
    value-=1
    digits[nonTidyIndex] = str(value)
    # print 'new n: {}'.format(digits)
    # set the remaining digits to 9
    nonTidyIndex+=1
    for x in range(nonTidyIndex, numDigits):
        digits[x] = '9'
    # print 'new n: {}'.format(digits)
    if digits[0] == '0':
        digits = digits[1:]
    return ''.join(digits)


for t in range(T):
    print '---------------------'
    line = f.readline()
    N = line.strip()
    print 'N: {}'.format(N)

    if (isTidy(N)):
        output = 'Case #{}: {}'.format((t+1), N)
        print output
        outFile.write(output + "\n")
    else:
        tidy = getTidy(N)
        while not isTidy(tidy):
            tidy = getTidy(tidy)
            # print 'tidy: {}'.format(tidy)

        output = 'Case #{}: {}'.format((t+1), tidy)
        print output
        outFile.write(output + "\n")
