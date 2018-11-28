def is_palindrome(num):
    strnum = str(num)
    numlen = len(strnum)
    
    for i in xrange(numlen / 2):
        if strnum[i] != strnum[numlen-1-i]:
            return 0
    
    return 1

n = input()

for i in xrange(n):
    line = raw_input().split(' ')
    min = int(line[0])
    max = int(line[1])
    count = 0
    case = i+1

    square_palindromes = []
    for i in xrange(0, min):
        if is_palindrome(i):
            square_palindromes.append(i*i)
    
    for i in xrange(min, max+1):
        if is_palindrome(i):
            square_palindromes.append(i*i)
            if i in square_palindromes:
                count += 1

    print 'Case #%d: %d' % (case, count)