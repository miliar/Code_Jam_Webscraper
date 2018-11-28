import sys

def calculate_reused(a, b, n):
    number = str(n)
    candiates = set([int(number[i:]+number[:i]) for i in range(1, len(number))])
    reused = 0
    for candiate in candiates:
        if candiate < a or candiate <= n or candiate > b:
            continue
        reused += 1
    return reused

num_cases = int(sys.stdin.readline())
for i, line in zip(range(1, num_cases + 1), sys.stdin):
    splitted = line.split(' ')
    a = int(splitted[0])
    b = int(splitted[1])
    reused = 0
    for n in range(a, b + 1):
        reused += calculate_reused(a, b, n)
    print "Case #%d: %d" % (i, reused)
