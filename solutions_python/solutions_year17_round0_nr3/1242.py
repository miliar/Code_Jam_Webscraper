# from bisect import bisect_left, bisect_right, insort
from collections import Counter
#
#
# def index(a, x):
#     'Locate the leftmost value exactly equal to x'
#     i = bisect_left(a, x)
#     if i != len(a) and a[i] == x:
#         return i
#     raise ValueError
#
# def find_lt(a, x):
#     'Find rightmost value less than x'
#     i = bisect_left(a, x)
#     if i:
#         return a[i-1]
#     raise ValueError
#
# def find_le(a, x):
#     'Find rightmost value less than or equal to x'
#     i = bisect_right(a, x)
#     if i:
#         return a[i-1]
#     raise ValueError
#
# def find_gt(a, x):
#     'Find leftmost value greater than x'
#     i = bisect_right(a, x)
#     if i != len(a):
#         return a[i]
#     raise ValueError
#
# def find_ge(a, x):
#     'Find leftmost item greater than or equal to x'
#     i = bisect_left(a, x)
#     if i != len(a):
#         return a[i]
#     raise ValueError
#
#
#
# def rl(stalls, location):
#     l = location - find_le(stalls, location) - 1
#     r = find_ge(stalls, location) - location - 1
#     return l, r
#
#
# def solve_old(n_stalls, people):
#     taken = [0,n_stalls + 1]
#     last = None
#     for person in range(people):
#         print(*["O" if x in taken else "." for x in range(0, n_stalls+2)], sep="")
#         # print(*rls)
#         def selector(stall):
#             r, l = rl(taken, stall)
#             return r < 0, l < 0, -min(r, l), -max(r, l), stall
#
#         # print(*map(selector, range(1, 1+n_stalls)))
#         choice = min(list(range(1, 1+n_stalls)), key=selector)
#         last = rl(taken, choice)
#         insort(taken, choice)
#     print(*["O" if x in taken else "." for x in range(0, n_stalls + 2)], sep="")
#     l,r = last
#
#     return max(l,r), min(l,r)


def divide(x):
    x -= 1
    if x % 2 == 0:
        return x//2, x//2
    return x//2, x//2 + 1

def solve(n_stalls, people):
    openings = Counter([n_stalls])
    for person in range(people -1):
        biggest = max(openings)
        openings[biggest] -= 1
        openings = +openings # remove zeros
        for side in divide(biggest):
            openings[side] += 1
    last = max(openings)
    l, r = divide(last)
    return max(l, r), min(l, r)

def main():
    t = int(input())
    for case in range(1, 1 + t):
        stalls, people = map(int, input().split())
        low, high = solve(stalls, people)
        print(f"Case #{case}: {low} {high}")

if __name__ == '__main__':
    main()
