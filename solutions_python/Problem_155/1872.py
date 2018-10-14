#!/usr/bin/env python
import fileinput

def is_ovation(arr):
    claps = 0
    for level in range(0, len(arr)):
        if level == 0:
            claps += arr[level]
        else:
            claps += arr[level] if claps >= level else 0

    if claps == sum(arr):
        return True
    return False

def increment(arr, num):
    left = num
    for i in range(0, len(arr)):
        if left <= 0:
            break
        add = min(9 - arr[i], left)
        arr[i] += add
        left -= add
    return arr

def compute(arr):
    claps = 0
    extras = 0
    for level in range(0, len(arr)):
        if level == 0:
            claps += arr[level]
        else:
            if arr[level] == 0:
                continue
            elif claps >= level:
                claps += arr[level]
            else:
                delta = level - claps
                claps += delta
                extras += delta
                arr = increment(arr, delta)
                claps += arr[level]
    return extras

def main():
    num_runs = None
    n = 1
    for line in fileinput.input():
        if num_runs is None:
            num_runs = int(line)
            if num_runs <= 0:
                break
            else:
                continue

        max_level, tally = line.split(' ')
        max_level = int(max_level.strip())
        tally = [int(t) for t in tally.strip()]

        print "Case #%d: %d" % (n, compute(tally))
        n += 1
        if n >num_runs:
            break

if __name__ == "__main__":
    main()
