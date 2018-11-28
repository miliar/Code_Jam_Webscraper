import sys

def is_palindromes(num):
    digits = []
    if num == 0:
        digits.append(0)    
    while num > 0:
        digits.append(num % 10)
        num /= 10
    l = len(digits)
    for i in xrange(0,l/2):
        if digits[i] != digits[l-1-i]:
            return False
    return True    

num_case = int(sys.stdin.readline())

for case_id in xrange(1,num_case+1):
    a, b = map( int, sys.stdin.readline().split() )
    num_fair_square = 0
    for num in xrange(a,b+1):
        sqrt = num**0.5
        if int(sqrt) == sqrt:
            if is_palindromes(num) and is_palindromes(int(sqrt)):
                num_fair_square += 1
    print "Case #%s: %s" % (case_id, num_fair_square)
    