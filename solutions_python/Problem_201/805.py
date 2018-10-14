
def solve(n, k):

    groups = {n: 1}

    while True:
        nextCut = max(groups.keys())

        if groups[nextCut] >= k:
            if nextCut % 2 == 1:
                return [(nextCut - 1) / 2, (nextCut - 1) / 2]
            else:
                return [nextCut / 2, (nextCut / 2) - 1]

        numberSpaces = groups.pop(nextCut)

        if nextCut % 2 == 1:
            groups[(nextCut - 1) / 2] = groups.get((nextCut - 1) / 2, 0) + numberSpaces * 2
        else:
            groups[(nextCut / 2) - 1] = groups.get((nextCut / 2) - 1, 0) + numberSpaces
            groups[nextCut / 2] = groups.get(nextCut / 2, 0) + numberSpaces

        k -= numberSpaces


def main():

    numToCheck = []

    for i in range(0, int(raw_input())):

        newList = []

        numToCheck.append(raw_input().split(' '))

    count = 0
    for n, k in numToCheck:
        count += 1
        ret = solve(int(n), int(k))

        print("Case #{0}: {1} {2}".format(count, ret[0], ret[1]))


if __name__ == "__main__":
    main()