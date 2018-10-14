#!/usr/bin/env python3

def read_int():
    return int(input())

def largest_tidy(n):
    digits = [int(i) for i in str(n)]
    while True:
        for i in range(0, len(digits) - 1):
            if digits[i] > digits[i+1]:
                digits[i] -= 1
                for j in range(i+1, len(digits)):
                    digits[j] = 9
                break
        else:
            break
    result = 0
    for d in digits:
        result *= 10
        result += d
    return result

def main():
    ncases = read_int()
    for i in range(1, ncases + 1):
        n = read_int()
        print('Case #%d: %d' % (i, largest_tidy(n)))

if __name__ == '__main__':
    main()

