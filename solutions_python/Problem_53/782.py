#!/usr/bin/python

def main():
    ncases = int(raw_input())
    for i in range(1, ncases + 1):
        n, k = [ int(x) for x in raw_input().split() ]
        if k % 2**n == 2**n - 1:
            print "Case #" + str(i) + ": ON"
        else:
            print "Case #" + str(i) + ": OFF"

if __name__ == "__main__":
    main()
