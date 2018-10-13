def solveOne(case):
    def toInt(array):
        out = 0
        for digit in array:
            out = (10*out) + digit
        return str(out) if out > 0 else ''

    num = list(map(int, input().strip()))

    cstStart = 0
    for pos in range(1, len(num)):
        if num[pos-1] > num[pos]:  # decreasing point
            num[cstStart] -= 1  # it cannot be 0 (but can reach 0 now)
            return toInt(num[:cstStart+1]) + '9' * (len(num) - cstStart - 1)
        elif num[pos-1] != num[pos]:
            cstStart = pos

    # If we reach here, our number was increasing
    return toInt(num)


if __name__ == '__main__':
    numCases = int(input())
    for case in range(1, numCases+1):
        print("Case #{}: {}".format(case, solveOne(case)))
