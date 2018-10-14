# Seive it.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in arr:
    arr.extend([i * 10 + j for j in range(i % 10, 10)])
    if arr[-1] > 10 ** 19:
        break


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
            return key

    if low < 0:
        return arr[high]
    else:
        if low - 1 < 0:
            return arr[low]
        return arr[low - 1]


def solve():
    n = int(raw_input())
    return bs(arr, n)


def main():
    tc = int(raw_input())
    for i in xrange(tc):
        ans = solve()
        print "Case #{}: {}".format(i + 1, ans)


if __name__ == '__main__':
    main()
