inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "
    n, k = [int(x) for x in inf.readline().split()]
    size = n
    low = 1
    high = 0
    mind = 0
    maxd = 0
    while k > 0:
        if k > high:
            k -= high
        else:
            mind = size // 2
            maxd = (size + 1) // 2
            break
        if k > low:
            k -= low
        else:
            mind = (size - 1) // 2
            maxd = size // 2
            break
        if (size - 1) % 2 == 0:
            low = low * 2 + high
        else:
            high = high * 2 + low
        size = (size - 1) // 2
    rstr += str(maxd) + ' ' + str(mind)
    print(rstr)
    outf.write(rstr + '\n')
