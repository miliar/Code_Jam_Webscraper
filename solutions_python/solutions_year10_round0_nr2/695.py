import math

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    while b:
        a, b = b, a % b
    return a

def outputCase(number, output, file):
    file.write("Case #{0}: {1}\n".format(number + 1, output))

if __name__ == '__main__':
    inFile = open('B-small-attempt0.in', 'r')
    outFile = open('B-small.out', 'w')
    numCases = int(inFile.readline())
    print('There are', numCases, 'cases')

    for i in range(numCases):
        t = [int(x) for x in inFile.readline().split()]
        print(t.pop(0), t)
        m = min(t)
        print(m)
        d = [x - m for x in t]
        e = [x for x in d]
        print(e)
        while len(e) > 1:
            e.append(gcd(e.pop(0), e.pop(0)))
        g = e[0]
        print(g)
        r = [0 if x % g == 0 else g - x % g for x in t]
        print(r[0])
        outputCase(i, r[0], outFile)
        print()

    inFile.close()
    outFile.close()
    print('done')
