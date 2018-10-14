import sys

number = sys.stdin.readline()
test_cases = int(number)

def isPalindrome(n):
    l = str(n)
    if l == l[::-1]:
        return True

    return False

def countFairAndSquare(start, a, b):
    count = 0
    while 1:
        if isPalindrome(start):
            squared = start * start
            if squared >= a and squared <= b:
                if isPalindrome(squared):
                    count += 1
            elif squared > b:
                return count
        start += 1

        if start > 1000 and start > 21 * 10 ** (len(str(start)) - 2):
            start = 10 ** (len(str(start)))

for test_no in range(1, test_cases + 1):
    line = sys.stdin.readline().split(" ")
    A = line[0]
    B = line[1]

    if len(B) <= 16:
        a = int(A)
        b = int(B)
        start = 10 ** ((len(A) - 1) / 2)
        print "Case #"+ str(test_no) + ":", str(countFairAndSquare(start, a, b))

    elif len(A) < 16:
        a = int(A)
        b = 10 ** 16
        start = 10 ** ((len(A) - 1) / 2)

        print "Case #"+ str(test_no) + ":", str(countFairAndSquare(start, a, b))
