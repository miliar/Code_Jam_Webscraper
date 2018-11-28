import math

def main():
    inFile = open('c:\jam\D-large.in')

    T = int(inFile.readline())

    r = []
    for i in range(0, T):
        k = int(inFile.readline())
        line = inFile.readline()

        z = map(int, line.split())
        x = [zz for zz in z]
        x.sort()

        print z
        print x

        res = 0
        for i in range(0, len(z)):
            if z[i] != x[i]:
                res += 1

        r.append(res)
        print res

    outFile = open('c:\jam\D-large.out', 'w')
    for i in range(0, T):
        outFile.write('Case #%d: %f\n' % ((i+1), r[i]))
    outFile.close


if __name__ == '__main__':
    main()

