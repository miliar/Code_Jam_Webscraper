import sys

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    ifd = open(input_filename, 'r')
    ofd = open(output_filename, 'w')

    N = int(ifd.readline())

    for n in range(N):
        line = ifd.readline().split()
        P = int(line[0])
        K = int(line[1])
        L = int(line[2])

        line = ifd.readline().split()
        letterList = []
        for l in line:
            letterList.append(int(l))

        letterList.sort()
        letterList.reverse()

        c = 0

        for i in range(L):
            c += ((i / K + 1) * letterList[i])
        ofd.write("Case #%d: %d\n" % (n + 1, c))


    ifd.close()
    ofd.close()


main()