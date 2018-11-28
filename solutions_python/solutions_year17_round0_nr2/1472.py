#!/usr/bin/env python3


def main():
    t = int(input())  # read the number of test cases

    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, greatestTidyNumberLte(s)))


def greatestTidyNumberLte(s):
    digits = [int(x) for x in s]
    maxVal = maxIdx = -1
    for i, v in enumerate(digits):
        if v > maxVal:
            maxVal = v
            maxIdx = i
        elif v < maxVal:
            return decrementDigitsAtIdx(digits, maxIdx)
    return s


def decrementDigitsAtIdx(digits, idx):
    digits[idx] -= 1
    for i, v in enumerate(digits[idx + 1:], idx + 1):
        digits[i] = 9
    return "".join(str(x) for x in digits).lstrip("0")


main()
