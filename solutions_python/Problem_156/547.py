import sys
import math

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        D = int(sys.stdin.readline())
        pancakes = map(float, sys.stdin.readline().split())
        maxcakes = int(max(pancakes))
        mintime = maxcakes
        for i in range(1, maxcakes+1):
            time = i
            for n in pancakes:
                time += math.ceil(n / i) - 1
            mintime = min(mintime, time)
        print "Case #%d:" % t, int(mintime)

if __name__ == "__main__":
    main()
