import math

def main():
    inFile = open('c:\jam\C-large.in')

    T = int(inFile.readline())

    r = []
    for i in range(0, T):
        k = int(inFile.readline())
        line = inFile.readline()

        z = map(int, line.split())
        z.sort()

        s = 0
        for v in z:
            s = s ^ v
            
        if s == 0:
            res = str(sum(z[1:]))
        else:
            res = 'NO'

        r.append(res)
        print res

    outFile = open('c:\jam\C-large.out', 'w')
    for i in range(0, T):
        outFile.write('Case #%d: %s\n' % ((i+1), r[i]))
    outFile.close


if __name__ == '__main__':
    main()

