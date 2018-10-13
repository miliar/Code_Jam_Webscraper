#!/usr/bin/env python3

import sys

def read():
    return sys.stdin.readline().strip()

def swap_chars(s):
    return s.replace("+", "!").replace("-", "+").replace("!", "-")

def do_flip(s, i, k):
    return s[:i] + swap_chars(s[i:i+k]) + s[i+k:]

def flips_needed(s, k):
    count = 0
    for i in range(0, len(s)-k+1):
        if s[i] == '-':
            s = do_flip(s, i, k)
            count += 1

    if all(ch == '+' for ch in s):
        return count
    else:
        return "IMPOSSIBLE"

def main():
    num_cases = int(read())
    for i in range(num_cases):
        s, k = read().split(" ")
        k = int(k)

        print("Case #{}: {}".format(i+1, flips_needed(s, k)))
        sys.stdout.flush()

if __name__ == '__main__':
    main()

