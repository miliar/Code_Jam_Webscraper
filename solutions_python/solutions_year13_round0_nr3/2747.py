import math

def is_palindrome(n):
    n = str(n)
    return n == ''.join(reversed(n))

def input():
    with open('c.in') as file:
        tests_count = int(file.readline().strip())
        for i in xrange(tests_count):
            a, b = map(int, file.readline().split())
            yield a, b

def output(results):
    with open('c.out', 'w') as file:
        file.writelines('Case #%s: %s\n' % (i + 1, r) for i, r in enumerate(results))

def solve(input_sequence):
    for a, b in input_sequence:
        start, end = int(math.ceil(math.sqrt(a))), int(math.floor((math.sqrt(b))))
        count = 0
        for n in xrange(start, end + 1):
            if is_palindrome(n) and is_palindrome(n ** 2):
                count += 1
        yield count

if __name__ == '__main__':
    output(solve(input()))