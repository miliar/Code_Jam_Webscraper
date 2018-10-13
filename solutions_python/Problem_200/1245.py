
import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    numbers = list(map(int, list(sys.stdin.readline().strip())))

    changed = True
    while changed:
        changed = False
        for j in range(0, len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j] -= 1
                for k in range(j+1, len(numbers)):
                    numbers[k] = 9
                changed = True
                break

    print("Case #%d: %s" % ((i+1),''.join(map(str, numbers)).lstrip("0")))