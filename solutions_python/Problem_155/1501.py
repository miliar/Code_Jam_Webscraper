#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    t = input()
    for _ in range(t):
        s, audience = raw_input().split()
        people = 0
        ans = 0

        for i, c in enumerate(audience):
            if i > people:
                ans += i - people
                people = i
            people += int(c)
        print("Case #{}: {}".format(_+1, ans))




if __name__ == "__main__":
    main()
