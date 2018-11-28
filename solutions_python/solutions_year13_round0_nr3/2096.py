import gmpy

test_count = int(raw_input())

def is_palindrome(number):
    tested_string = str(number)
    return tested_string == tested_string[::-1]

for i in range(test_count):
    interval = map(int, raw_input().split(' '))
    
    palindromes = 0
    for num in range(interval[0], interval[1] + 1):
        if is_palindrome(num) and gmpy.is_square(num) and is_palindrome(gmpy.sqrt(num)):
            palindromes += 1
    print "Case #{0}: {1}".format(i + 1, palindromes)
