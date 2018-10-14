#!/usr/bin/env python3

def solve(c, s):
    if s == '':
        return ''
    if c <= s[0]:
        r = solve(s[0], s[1:])
        if r != None:
            return s[0] + r
    if c < s[0]:
        return chr(ord(s[0]) - 1) + ''.join('9' for _ in s[1:])
    else:
        return None

def main():
    t = int(input())
    for ti in range(t):
        s = input() # as string (!)
        print("Case #{}: {}".format(ti+1, solve('0', s).lstrip('0')))

if __name__ == '__main__':
    main()
