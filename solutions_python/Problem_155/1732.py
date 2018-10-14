#!/usr/bin/python
# cat testset.in | ./main.py > testset.out
# type testset.in | C:\Python34\python.exe a.py > testset.out
import sys


def main():
    t = int(sys.stdin.readline())
    for c in range(1, t + 1):
        sys.stdout.write("Case #" + str(c) + ": ")

        (smax, bins) = tuple(sys.stdin.readline().split())
        friends = 0
        standing = 0
        i = 0
        for s in bins:
            if standing < i:
                friends  += (i - standing)
                standing += (i - standing)
            standing += int(s)
            i += 1
        print(str(friends))


if __name__ == "__main__":
    main()