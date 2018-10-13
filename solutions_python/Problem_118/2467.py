import sys

def is_palindrome(num):
    return num == num[::-1]

# (kind of) babylonian method - see wikipedia
def is_square(num):
    x = num // 2
    check = set([x])
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in check:
            return False
        check.add(x)
    return True

# newton method - see wikipedia
def isqrt(n):
    q, r = divmod(n.bit_length(), 2)
    x = 2**(q + r)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y

finput = open(sys.argv[1], 'r')
foutput = open('output', 'w')

num = int(finput.readline())

for i in range(num):
    span = finput.readline()[:-1].split(' ')
    a, b = int(span[0]), int(span[1])

    res = 0
    for x in range(a, b + 1):
        if x == 1 or (is_palindrome(str(x)) and is_square(x)):
            if is_palindrome(str(isqrt(x))):
                res += 1

    foutput.write('Case #%d: %d\n' % ((i + 1), res))

finput.close()
foutput.close()