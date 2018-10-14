#!/usr/bin/python
# cat testset.in | ./main.py > testset.out
# type testset.in | C:\Python34\python.exe a.py > testset.out
import math
import sys


def main():
    t = int(sys.stdin.readline())
    for c in range(1, t + 1):
        sys.stdout.write("Case #" + str(c) + ": ")

        (x, r, c) = map(int, tuple(sys.stdin.readline().split()))
        # min and max length of an L shaped piece
        lmax = math.ceil(float((x-1))/2.0) + 1
        lmin = math.floor(float((x-1))/2.0) + 1

        # Special cases - for faster processing
        if ( ((r*c) % x != 0)            # area not evenly divisible
          or (lmin > r or lmin > c)      # L shaped piece (short side) won't fit on board 
          or (lmin == r and lmax > c)    # L shaped piece (long side) won't fit on the board
          or (lmin == c and lmax > r)   
          or (x > 7)                     # create a donut piece
          or (x == 4 and r == 2)         # use an s piece, which will devide the board into two halves with odd units
          or (x == 4 and c == 2)
           ):
            print("RICHARD")
            continue

        if x <= 4:
            print("GABRIEL") 
            continue

        # General case
        print("UNKNOWN x={0}, r={1}, c={2}".format(x, r, c))


if __name__ == "__main__":
    main()