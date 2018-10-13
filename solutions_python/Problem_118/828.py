#!/usr/bin/env python
def count(numDigits):
    if numDigits % 2 == 0:
        e = numDigits/2 - 1
        # 100...
        # 200...
        total = 2
        cur = e
        if e > 0:
            # 1100...
            total += cur
        if e > 1:
            # 11100...
            cur = cur * (e-1) / 2
            total += cur
        if e > 2:
            # 111100...
            cur = cur * (e-2) / 3
            total += cur
        return total
    else:
        e = ((numDigits+1) / 2) - 1
        # 100...
        # 200...
        total = 2
        if numDigits == 1:
            # 3
            total += 1
        if e > 0:
            # 1002...
            # 2001...
            total += 2
            # 1100...
            total += e
        if e > 1:
            # 11100...
            total += e * (e-1) / 2
            # 11002...
            total += e-1
        if e > 2:
            # 111100...
            total += e * (e-1) * (e-2) / 6
        if e > 3:
            # 1111001...
            total += (e-1) * (e-2) * (e-3) / 6
        return total

def generateAll(numDigits):
    all = []
    if numDigits % 2 == 0:
        e = numDigits/2 - 1
        # 100...
        # 200...
        all.append('1' + '0' * e)
        all.append('2' + '0' * e)
        if e > 0:
            # 1100...
            for i in range(e):
                all.append('1' + '0' * i + '1' + '0' * (e-i-1))
        if e > 1:
            # 11100...
            for i in range(e):
                for j in range(e-i-1):
                    all.append('1' + '0' * i + '1' + '0' * j + '1' + '0' * (e - i - j - 2))
        if e > 2:
            # 111100...
            for i in range(e):
                for j in range(e-i-1):
                    for k in range(e-i-j-2):
                        all.append('1' + '0' * i + '1' + '0' * j + '1' + '0' * k + '1' + '0' * (e - i - j - k - 3))
        return map(lambda(x): int(x + x[::-1]), all)
    else:
        e = ((numDigits+1) / 2) - 1
        # 100...
        # 200...
        all.append('1' + '0' * e)
        all.append('2' + '0' * e)
        if numDigits == 1:
            all.append('3')
        if e > 0:
            # 1002...
            # 2001...
            all.append('1' + '0' * (e-1) + '2')
            all.append('2' + '0' * (e-1) + '1')
            # 1100...
            for i in range(e):
                all.append('1' + '0' * i + '1' + '0' * (e-i-1))
        if e > 1:
            # 11100...
            for i in range(e):
                for j in range(e-i-1):
                    all.append('1' + '0' * i + '1' + '0' * j + '1' + '0' * (e - i - j - 2))
            # 11002...
            for i in range(e-1):
                all.append('1' + '0' * i + '1' + '0' * (e-i-2) + '2')
        if e > 2:
            # 111100...
            for i in range(e):
                for j in range(e-i-1):
                    for k in range(e-i-j-2):
                        all.append('1' + '0' * i + '1' + '0' * j + '1' + '0' * k + '1' + '0' * (e - i - j - k - 3))
        if e > 3:
            # 1111001...
            for i in range(e):
                for j in range(e-i-1):
                    for k in range(e-i-j-2):
                        all.append('1' + '0' * i + '1' + '0' * j + '1' + '0' * k + '1' + '0' * (e - i - j - k - 4) + '1')
        if numDigits > 1:
            return map(lambda(x): int(x + x[len(x)-2::-1]), all)
        else:
            return map(int, all)

def countFloor(numDigits, floor):
    all = generateAll(numDigits)
    #print 'floor'
    #print all
    #print floor, numDigits
    total = 0
    for i in all:
        if i*i >= floor:
            total += 1
    return total

def countCeiling(numDigits, ceiling):
    all = generateAll(numDigits)
    #print 'ceil'
    #print all
    total = 0
    for i in all:
        if i*i <= ceiling:
            total += 1
    return total

def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines

def process_lines(lines):
    ans = []
    first = True
    numCases = int(lines[0])
    lineIndex = 1
    for caseIndex in range(numCases):
        case = []
        ab = lines[lineIndex].split(' ')
        a = int(ab[0])
        b = int(ab[1])
        lineIndex += 1
        ans.append((a, b))
    return ans

def process_case(case):
    a = case[0]
    b = case[1]
    strA = str(a)
    strB = str(b)
    total = 0
    lower = (len(strA) + 2) / 2
    higher = (len(strB) + 2) / 2
    for i in range(lower, higher + 1):
        total += count(i)
    #print a, b, total
    total -= countCeiling(lower, a - 1)
    #print total
    total -= countFloor(higher, b + 1)
    #print total
    return total

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    lines = process_file(filename)
    cases = process_lines(lines)
    c = 0
    for case in cases:
        c += 1
        print "Case #%d: %s" % (c, process_case(case))