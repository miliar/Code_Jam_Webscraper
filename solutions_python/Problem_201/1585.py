from collections import defaultdict


def getlsrs(num):
    ls = rs = num >> 1
    if num % 2 == 0:
        ls -= 1
    return ls, rs


def bs(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid

    return low


def solvefor(S, P):
    if S == P:
        return 0, 0

    # Init
    intervals = [S]
    countMap = defaultdict(lambda: 0)
    countMap[S] = 1

    for i in xrange(P):
        chosen = intervals[-1]
        countMap[chosen] -= 1
        if countMap[chosen] == 0:
            del countMap[chosen]
            intervals.pop()

        if i == P - 1:
            ls, rs = getlsrs(chosen)
            return max(ls, rs), min(ls, rs)

        if chosen == 1:
            pass
        elif chosen == 2:
            countMap[1] += 1
            if countMap[1] == 1:
                intervals.insert(0, 1)
        else:
            ls, rs = getlsrs(chosen)
            countMap[ls] += 1
            if countMap[ls] == 1:
                ind = bs(intervals, ls)
                intervals.insert(ind, ls)
            countMap[rs] += 1
            if countMap[rs] == 1:
                ind = bs(intervals, rs)
                intervals.insert(ind, rs)


def solve():
    S, P = map(int, raw_input().split())
    return solvefor(S, P)


def main():
    tc = int(raw_input())
    for i in xrange(tc):
        ans = solve()
        print "Case #{}: {} {}".format(i + 1, ans[0], ans[1])


if __name__ == '__main__':
    main()
