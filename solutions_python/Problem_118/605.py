import math

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

def solve2(line):
    A, B = (int(x) for x in line.split())
    start = int(math.floor(math.sqrt(A)) - 1)
    end = int(math.ceil(math.sqrt(B)) + 1)
    count = 0
    for x in range(start, end + 1):
        if is_palindrome(x):
            square = x * x
            if is_palindrome(square):
                if A <= square <= B:
                    count += 1
                    print square
    return count

cache = [
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
]

def solve(line):
    A, B = (int(x) for x in line.split())
    count = 0
    for number in cache:
        if A <= number <= B:
            count += 1
    return count

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()