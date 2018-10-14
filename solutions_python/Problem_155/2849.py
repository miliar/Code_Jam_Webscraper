#!/usr/bin/python


def readfile(filename):

    cases = list(list())
    with open(filename, 'r') as f:
        numTests = int(f.readline())
        print numTests
        for i in range(numTests):
            cases.append([int(x) for x in f.readline().split()[1]])

        return cases


def writeFile(solution, filename):

    with open(filename, 'w') as f:
        for idx, friends in enumerate(solution):
            f.write("Case #{}: {}\n".format(idx + 1, friends))

if __name__ == "__main__":
    cases = readfile("tests/example.txt")
    print(cases)
