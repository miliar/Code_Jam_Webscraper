def main():
    input = open('B-large.in', 'r')
    numCases = int(input.readline().strip())

    case = 0

    for line in input:
        case = case + 1
        calcTidy(line, case)

def calcTidy(lastNum, case):
    lastNumRev = lastNum[::-1].strip()

    out = []

    for num in lastNumRev:
        val = int(num)
        out.insert(0, val)

        if (len(out) > 1 and out[0] > out[1]):
            out = fixItUp(out)

    retVal = "".join(map(str, out)).lstrip("0")

    print "Case #{0}: {1}".format(case, retVal)

def fixItUp(arr):
    arr[0] = arr[0] - 1
    for x in range(1, len(arr)):
        arr[x] = 9
    return arr

if __name__ == '__main__':
    main()