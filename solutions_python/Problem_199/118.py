#!/usr/bin/env python

def Solve(arr, k):
    cnt = 0
    for i, val in enumerate(arr):
        if val == 1:
            continue
        if len(arr) - k < i:
            return 'IMPOSSIBLE'
        cnt += 1
        for j in xrange(i+1, i+k):
            arr[j] = -1*arr[j]
    return str(cnt)

def main():
    with open("a_small.txt") as _in, open("a_small_out.txt", "w") as _out:
        i = -1
        for line in _in:
            i += 1
            if i == 0:
                continue
            arrStr, kStr  = line.split(" ")
            k = int(kStr)
            arr = [-1 if ch == '-' else 1 for ch in arrStr]
            res = Solve(arr, k)
            _out.write("Case #" + str(i) + ": " + res + "\n")


if __name__ == "__main__":
    main()
