from collections import defaultdict

def main():
    input = open('C-large.in', 'r')
    numCases = int(input.readline().strip())

    case = 0

    for line in input:
        case = case + 1
        n, k = line.strip().split()
        bathroomTime(int(n), int(k), case)

def bathroomTime(N, K, case):
    extents = defaultdict(int)
    extents[N] = 1

    total = 0

    keys = set([N])

    while total < K:
        nextKey = max(keys)
        keys.remove(nextKey)
        num = extents[nextKey]
        if nextKey % 2 == 0:
            extents[nextKey // 2] += num
            extents[(nextKey // 2) - 1] += num
            keys.add(nextKey // 2)
            keys.add((nextKey // 2) - 1)
        else:
            extents[nextKey // 2] += num*2
            keys.add(nextKey // 2)
        total += num*2

    sortedExtents = sorted(extents.items(), key=lambda x: x[0], reverse=True)

    sum = 0
    bigThing = 0
    while sum < K:
        bigThing, num = sortedExtents.pop(0)
        sum += num

    print "Case #{0}: {1} {2}".format(case, bigThing // 2, bigThing - 1 - (bigThing // 2))


if __name__ == '__main__':
    main()