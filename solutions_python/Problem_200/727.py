#!/usr/bin/python3

def tidy(num):
    if len(num) <= 1: return num
    prev = tidy(num[1:])
    if num[0] <= prev[0]: return num[0]+prev
    else:
        antes = str(int(num[0])-1)
        return antes + ('9'*len(prev))


if __name__ == "__main__":
    N = int(input())
    for i in range(1, N+1):
        print("Case #%d: %d"%(i, int(tidy(input()))))
