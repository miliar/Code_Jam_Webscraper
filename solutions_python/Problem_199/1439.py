import sys

def parse():
    NT = int(input())

    testCases = []
    for i in range(1, NT + 1):
        L, n = input().split(" ")
        n = int(n)
        L = list(map(lambda x: True if x=="+" else False, L))
        testCases.append((L, n))

    return testCases


def getMinimumFlips(inBoolList, n):
    flips = 0
    for i in range(len(inBoolList) - (n-1)):
        if inBoolList[i] is True:
            continue
        else:
            # Flip
            inBoolList[i:(i+n)] = list(map(lambda x: not x, inBoolList[i:(i+n)]))
            flips += 1

    # Make sure that there are no 'false' values in the last window
    if not all(inBoolList[-1*n:]):
        return None
    else:
        return flips


def main():
    testCases = parse()
    for i, t in enumerate(testCases):
        solution = getMinimumFlips(*t)
        if solution is None:
            print("Case #{0}: IMPOSSIBLE".format(i+1))
        else:
            print("Case #{0}: {1}".format(i+1, solution))

if __name__ == '__main__':
    main()
