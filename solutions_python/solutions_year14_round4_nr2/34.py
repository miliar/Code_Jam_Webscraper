__author__ = 'dan'

def validate(numbers):
    if len(numbers) < 1:
        return True
    lt = True
    for i in range(1, len(numbers)):
        if lt and numbers[i-1] < numbers[i]:
            continue
        elif not lt and numbers[i-1] > numbers[i]:
            continue
        elif lt and numbers[i-1] > numbers[i]:
            lt = False
            continue
        else:
            return False
    return True

T = int(raw_input())
for case in range(1, T+1):
    cache = {}
    n = int(raw_input())
    numbers = map(int, raw_input().split())
    sortednumbers = sorted(numbers)

    leftpos, rightpos = 0, n-1

    swaps = 0

    for i in range(n):
        p = numbers.index(sortednumbers[i])
        if p - leftpos < rightpos - p:
            swaps += p - leftpos
            for j in reversed(range(leftpos, p)):
                numbers[j+1] = numbers[j]
            numbers[leftpos] = -1
            leftpos += 1
        else:
            swaps += rightpos - p
            for j in range(p, rightpos):
                numbers[j] = numbers[j+1]
            numbers[rightpos] = -1
            rightpos -= 1
        # print numbers

    print "Case #%d: %d" % (case, swaps)