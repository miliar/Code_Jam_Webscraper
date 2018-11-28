#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    T = input()
    ans = 0
    for t in range(1, T+1):
        R, C, W = map(int, raw_input().split())
        if W == 1:
            ans = R * C
        elif R == 1 and W == C:
            ans = W
        elif R == 1 and W == C-1:
            ans = C
        else:
            if C % W == 0:
                ans = (C / W) + (W-1)
            else:
                ans = (C / W) + W
        print("Case #{}: {}".format(t, ans))


if __name__ == "__main__":
    main()
