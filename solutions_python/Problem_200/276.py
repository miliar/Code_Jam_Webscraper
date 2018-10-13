#!/usr/bin/env python3

"""
Tidy Numbers

Author: Alex Dale - @SuperOxigen
"""

import fileinput

def getLargestTidy(digits):
    l = len(digits)

    for i in range(1, l-1):
        if digits[i] > digits[i+1]:

            if i == 1:
                for j in range(2, l):
                    digits[j] = 9
                digits[1] -= 1
                return

            for j in range(i):
                if digits[i-j] > digits[i-j-1]:
                    digits[i-j] -= 1
                    for k in range(i-j+1, l):
                        digits[k] = 9
                    return

def main():
    fin = fileinput.input()

    t = int(fin.readline().strip())

    for c in range(1, t+1):
        number = fin.readline().strip()
        l = len(number)

        digits = [0]
        digits.extend([int(d) for d in number])

        getLargestTidy(digits)

        tidy = sum([digits[l-i]*10**i for i in range(l)])

        print("Case #{}: {}".format(c, tidy))

if __name__ == "__main__":
    main()
