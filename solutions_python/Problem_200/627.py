from sys import stdin

T = int(stdin.readline())

for case in range(1, T+1):
    line = stdin.readline()
    result = ["Case #{}: ".format(case)]

    curSegment = None
    curCount = 0
    done = False

    for d in line.strip():
        if done:
            result.append('9')

        elif not curSegment:
            curSegment = d
            curCount = 1

        elif curSegment == d:
            curCount += 1

        elif d > curSegment:
            result.append(curSegment * curCount)
            curSegment = d
            curCount = 1

        else: # d < curSegment
            firstChar = str(int(curSegment) - 1)
            if firstChar != '0':
                result.append(firstChar)
            result.append('9' * curCount)
            curCount = 0
            curSegment = None
            done = True

    if curSegment:
        result.append(curSegment * curCount)

    print(''.join(result))

