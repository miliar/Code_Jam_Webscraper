import math, itertools

def isPalindrome(num):
    if len(str(num)) < 2:
        return True
    else:
        strnum = str(num)
        if strnum[0] != strnum[len(strnum)-1]:
            return False
        else:
            return isPalindrome(strnum[1:len(strnum)-1])

def numInRange(arange, brange):
    num_super_palindromes = 0
    for i in range(arange, brange + 1):
        if isPalindrome(i):
            j = math.sqrt(i)
            if j%1 == 0:
                j = int(j)
                if isPalindrome(j):
                    num_super_palindromes += 1
    return num_super_palindromes

f = open('C-small-attempt0.in')
test_cases = f.readline()
case = 1
o = open('out.txt', 'w')
for line in f:
    arange, brange = line.split(' ')
    arange = int(arange)
    brange = int(brange)
    o.write('Case #' + str(case) + ': ' + str(numInRange(arange, brange)) + '\n')
    case += 1
f.close()
o.close()
