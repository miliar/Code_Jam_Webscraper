import sys

def nline():
    line = sys.stdin.readline()
    return [int(n) for n in line.split()]

def ceil(a, b):
    return (a + b - 1) / b

def count_trips(r, n, shift):
    trips = [0] * n
    firstvisit = [-1] * n
    cur = 0
    steps = 1
    while True:
        if steps > r: # no loop
            return trips
        if firstvisit[cur] != -1: # loop found
            break
        trips[cur] = 1
        firstvisit[cur] = steps
        cur = (cur + shift[cur]) % n
        steps += 1

    # Process loop

    loop_length = steps - firstvisit[cur]
    loop_start = cur

    trips[cur] += ceil(r - steps + 1, loop_length)
    cur = (cur + shift[cur]) % n
    steps += 1
    while steps <= r and cur != loop_start:
        trips[cur] += ceil(r - steps + 1, loop_length)
        cur = (cur + shift[cur]) % n
        steps += 1

    return trips

t = nline()[0]

for testcase in range(1, t + 1):
    r, k, n = nline()
    g = nline()

    g = g + g # to avoid overflowing

    shift = []
    money = []

    for i in range(n):
        crowd = g[i]

        j = 1
        while True:
            if crowd + g[i + j] > k or j == n:
                shift.append(j)
                money.append(crowd)
                break
            crowd += g[i + j]
            j += 1

    #print shift, money

    trips = count_trips(r, n, shift)

    #print trips

    income = 0
    for i in range(n):
        income += money[i] * trips[i]

    print "Case #%d: %d" % (testcase, income)

