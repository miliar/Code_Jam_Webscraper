f = open("B-large.in")
fw = open("B-large.txt", 'w+')

testCases = 0   # test cases in the input file

first_line = f.readline()
testCases = int(first_line)

def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))

def checkTidyNumber(N):
    n = N
    digits = []

    while n:
        digit = n % 10
        digits.insert(0, int(digit))
        n = n / 10
        pass

    if is_sorted(digits):
        return 1
    else:
        last_digit = digits[0]
        for i in xrange(1, len(digits)):
            if digits[i] < last_digit:
                for j in xrange(i, len(digits)):
                    digits[j] = 0
                break
            
            last_digit = digits[i]
        num = int(''.join(map(str,digits)))
        return num
    pass

for case in xrange(0, testCases):

    line = f.readline()
    N = int(line)  # the last number counted by Tatiana

    checkNext = True
    while checkNext:
        status = checkTidyNumber(N)
        if status == 1:
            checkNext = False
        else:
            N = status - 1

    fw.write('Case #{}: {}\n'.format(case + 1, N))
f.close()
fw.close()
