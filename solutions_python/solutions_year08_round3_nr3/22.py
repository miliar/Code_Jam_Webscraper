import sys

def concise(cs):
    ncs = []
    l = -1
    c = 0
    for i in cs:
        if (i != l):
            if c != 0:
                ncs.append((l, c))
            l = i
            c = 1
        else:
            c += 1
    ncs.append((l, c))
    return ncs

def count(s):
    ns = []
    for i in s:
        if (i[1] != 0):
            ns.append([i[0], 0, i[1]])
    c = 0
    for i in range(len(ns)):
        for j in range(i, len(ns)):
            if (ns[i][0] < ns[j][0]):
                ns[j][1] += ns[i][2]
                c += ns[i][2]
    return ns, c

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    ifd = open(input_filename, 'r')
    ofd = open(output_filename, 'w')

    N = int(ifd.readline())

    for n in range(N):
        line = ifd.readline().split()
        CN = int(line[0])
        CM = int(line[1])
        CX = int(line[2])
        CY = int(line[3])
        CZ = int(line[4])
        CA = []
        CS = []
        for cm in range(CM):
            CA.append(int(ifd.readline()))

        for cn in range(CN):
            CS.append([int(CA[cn % CM]), 1])
            CA[cn % CM] = (CX * CA[cn % CM] + CY * (cn + 1)) % CZ

        totalc = len(CS);
        print CS
        while True:
            CS, c = count(CS)
            totalc += c
            if (c == 0):
                break

        print n + 1, totalc
        ofd.write("Case #%d: %d\n" % (n + 1, totalc % 1000000007))

    ifd.close()
    ofd.close()


main()