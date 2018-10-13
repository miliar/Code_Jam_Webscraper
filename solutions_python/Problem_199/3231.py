"""2k17 CodeJam First Question."""
import sys


def PancakeFlip(pancakes, flipper):
    """Find number of flips as per https://pastebin.com/weJUiwkF."""
    count = 0
    numberOfPancakes = len(pancakes)
    if numberOfPancakes < flipper:
        return "IMPOSSIBLE"
    for index in range(numberOfPancakes):
        if index == numberOfPancakes - (flipper - 1):
            break
        if pancakes[index] is True:
            continue
        else:
            if all(x == pancakes[index] for x in pancakes[index:(index + flipper)]) is True and pancakes[index] is True:
                count += 1
                continue
            else:
                pancakes[index:(index + flipper)] = [not i for i in pancakes[index:(index + flipper)]]
                count += 1
                continue
    if pancakes[0] is True and pancakes == [True] * numberOfPancakes:
        return count
    else:
        return "IMPOSSIBLE"


for i in range(int(input())):
    x = sys.stdin.readline().split()
    print("Case #" +
          str(i + 1) +
          ": " +
          str(PancakeFlip([True if i == '+' else False for i in x[0]], int(x[1]))))
