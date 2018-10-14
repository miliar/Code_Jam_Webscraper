import math


def generate_palindromes(maxn):
    l = range(10)
    m = 100
    lprev = l
    while m <= maxn:
        lnew = []
        for i in range(1, 10):
            for x in lprev:
                num = (m*i) + x*10 + i
                lnew.append(num)
        lprev = lnew
        l += lnew
        m *= 100

    result = l

    l = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    m = 1000
    lprev = l
    while m <= maxn:
        lnew = []
        for i in range(1, 10):
            for x in lprev:
                num = (m*i) + x*10 + i
                lnew.append(num)
        lprev = lnew
        l += lnew
        m *= 100

    result += l

    return result


def is_palindrome(n):
    num = n
    rev = 0

    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num / 10

    return n == rev


n = int(raw_input())
ranges = []

for _ in range(n):
    line = raw_input().split(' ')
    ranges.append([int(line[0]), int(line[1])])


case_index = 1
for r in ranges:
    A = r[0]
    B = r[1]

    count = 0

    palindromes = generate_palindromes(math.sqrt(B))
    squares = [x**2 for x in palindromes]
    result = [x for x in squares if is_palindrome(x)]
    result = [x for x in result if A <= x <= B]

    print "Case #%d: %d" % (case_index, len(result))
    case_index += 1
