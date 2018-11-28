from sys import stdin, stdout
import math

def is_palindrome(n):
    s = str(n)
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        s = s[1:-2]

    return True

line_count = int(stdin.readline())
for i in range(line_count):
    parts = stdin.readline().split(' ')
    start = int(parts[0])
    end = int(parts[1])

    count = 0
    for n in range(start, end+1):
        if not is_palindrome(n):
            continue
        rt = int(math.sqrt(n))
        if rt*rt != n or not is_palindrome(rt):
            continue
        count += 1

    print('Case #{}: {}'.format(i+1, count))
