import sys

# helpers

def readline():
    return sys.stdin.readline().strip()

def readints():
    return map(int, readline().split())

# process input

num_cases = int(readline())

for i in range(1, num_cases + 1):
    line = readints()
    n, s, p = line[:3]
    t = line[3:]

    always = 0
    when_surprising = 0

    for score in t:
        base = score / 3

        # not surprising: 3k -> k, 3k + 1 -> k + 1, 3k + 2 -> k + 1
        not_surprising = base + (1 if score % 3 != 0 else 0)

        # surprising: 3k + 2 -> k + 2, 3k + 0 -> k + 1, 3k + 1 -> k + 1
        surprising = base + (2 if score % 3 == 2 else 1)

        if not_surprising >= p:
            always += 1
        elif surprising >= p and 2 <= score <= 28:
            when_surprising += 1

    answer = always + min(when_surprising, s)

    print "Case #{0}: {1}".format(i, answer)


