def __main__():
    f = open("in.txt", 'r')
    o = open("out.txt", 'w')

    noOfCases = int(f.readline())
    for testNo in range(noOfCases):
        counter = 0
        data = f.readline()
        output = solver(data[:-1])
        output = int(output)
        o.write("Case #" + str(testNo + 1) + ": " + str(output) + "\n")


def solver(n):
    n = list(n)
    dex = inOrder(n)
    while dex != -1:
        n[dex] = str(int(n[dex]) - 1)
        n = n[:dex + 1] + ['9'] * (len(n) - dex - 1)
        dex = inOrder(n)
    return ''.join(n)


def inOrder(n):

    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return i
    return -1

if __name__ == '__main__':
    __main__()
