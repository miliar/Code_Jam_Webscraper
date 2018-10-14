
def outputCase(number, output, file):
    file.write("Case #{0}: {1}\n".format(number + 1, output))

if __name__ == '__main__':
    inFile = open('C-small-attempt0.in', 'r')
    outFile = open('C-small.out', 'w')
    numCases = int(inFile.readline())
    for bb in range(numCases):
        case = [int(x) for x in inFile.readline().split()]
        R = case[0]
        k = case[1]
        N = case[2]
        g = [int(x) for x in inFile.readline().split()]

        money = 0
        a = []
        for i in range(R):
            n = 0
            while len(g) != 0 and n + g[0] <= k:
                p = g.pop(0)
                money += p
                n += p
                a.append(p)
            for xx in a:
                g.append(xx)
            a = []
        outputCase(bb, money, outFile)
        print(money)
    inFile.close()
    outFile.close()
    print('done')
