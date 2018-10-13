def solve():
    cnt = 0
    s, k = raw_input().split()
    arr = list(s)
    k = int(k)
    for i in xrange(len(arr) - k + 1):
        if arr[i] == '+':
            continue
        else:
            cnt += 1
            for j in xrange(k):
                arr[i + j] = '+' if arr[i + j] == '-' else '-'
                # print arr

    if arr.count('-') > 0:
        cnt = 'IMPOSSIBLE'

    return cnt


def main():
    tc = int(raw_input())
    for i in xrange(tc):
        ans = solve()
        print "Case #{}: {}".format(i + 1, ans)


if __name__ == '__main__':
    main()
