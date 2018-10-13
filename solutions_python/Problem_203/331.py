#! python3

DATA_FILE = "A-large"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                R, C = [int(n) for n in line.split()]
                cake = []
                for i in range(R):
                    cake.append([c for c in in_file.readline().strip()])
                done = {'?'}
                for i in range(R):
                    for j in range(C):
                        letter = cake[i][j]
                        if letter not in done:
                            expand(i, j, cake)
                            done.add(letter)

                print("Case #{}:".format(x + 1), file=fout)
                for line in cake:
                    print(''.join(line), file=fout)

def expand(i, j, cake):
    letter = cake[i][j]
    ul = (i, j)
    lr = (i, j)
    test = (lr[0], lr[1] + 1)
    while clear(i, j, ul, test, cake):
        lr = test
        test = (lr[0], lr[1] + 1)

    test = (ul[0], ul[1] - 1)
    while clear(i, j, test, lr, cake):
        ul = test
        test = (ul[0], ul[1] - 1)

    test = (lr[0] + 1, lr[1])
    while clear(i, j, ul, test, cake):
        lr = test
        test = (lr[0] + 1, lr[1])

    test = (ul[0] - 1, ul[1])
    while clear(i, j, test, lr, cake):
        ul = test
        test = (ul[0] - 1, ul[1])

    for i in range(ul[0], lr[0] + 1):
        for j in range(ul[1], lr[1] + 1):
            cake[i][j] = letter


def clear(a, b, ul, lr, cake):
    if ul[0] < 0 or ul[1] < 0 or lr[0] >= len(cake) or lr[1] >= len(cake[0]):
        return False
    for i in range(ul[0], lr[0] + 1):
        for j in range(ul[1], lr[1] + 1):
            if i == a and j == b:
                continue
            if cake[i][j] != '?':
                return False
    return True

if __name__ == "__main__":
    main()
