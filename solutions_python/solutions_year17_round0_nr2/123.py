#!/usr/bin/env python

def Solve(arr):
    prev = -1
    useMax = False
    for i, val in enumerate(arr):
        if useMax:
            arr[i] = '9'
            continue
        cur = int(val)
        if cur >= prev:
            prev = cur
            continue
        j = i-1
        while j > 0 and int(arr[j])-1 < int(arr[j-1]):
            arr[j] = '9'
            j -= 1
        arr[j] = str(int(arr[j])-1)
        useMax = True
        arr[i] = '9'
    return "".join(arr if arr[0] != '0' else arr[1:])


def main():
    with open("b_small.txt") as _in, open("b_small_out.txt", "w") as _out:
        i = -1
        for line in _in:
            i += 1
            if i == 0:
                continue
            res = Solve(list(line.rstrip()))
            _out.write("Case #" + str(i) + ": " + res + "\n")

if __name__ == "__main__":
    main()
