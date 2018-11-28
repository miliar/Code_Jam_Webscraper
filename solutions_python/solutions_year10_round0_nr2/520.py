
def mcd(a, b):
    if b > a:
        tmp = a
        a = b
        b = tmp
    while b > 0:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r
    return a

inFile = open("B-large.in")
outFile = open("B-large.out", "w")

C = int(inFile.readline())
for nTestCase in range(1, C + 1):
    events = [int(num) for num in (inFile.readline().split())]
    N = events.pop(0)
    #events.sort(reverse = True)
    m = 0
    for i in range(N - 1):
        diff = abs(events[i] - events[i + 1])
        m = mcd(m, diff)
    if m == 0: raise "m is zero"
    y = (m - (events[0] % m)) % m
    outFile.write("Case #" + str(nTestCase) + ": " + str(y) + "\n")
