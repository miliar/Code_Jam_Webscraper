#!/usr/bin/env python3
def solver(n, k):
    seg = [n]
    for i in range(k):
        p = seg.pop()
        d = (p-1)//2
        q = p - d -1
        seg.append(d)
        seg.append(q)
        seg.sort()
    return q, d

def main():
    cases = int(input())
    for i in range(cases):
        n, k = [int(x) for x in input().split(' ')]
        n, k = solver(n, k)
        print("Case #{}: {} {}".format(i+1, n, k))

if __name__ == '__main__':
    main()