from operator import itemgetter
from math import pi

debug = False

def dbg_print(x):
    if debug:
        print(x)


def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        cakes = []
        for j in range(0, n):
            ri, hi = [int(s) for s in input().split(" ")]
            cakes.append( (ri, 2*ri*hi) )

        dbg_print("----------------------------------------")
        cakes.sort(reverse=True) # sorted by radius
        dbg_print(cakes)
        sol = 0
        for j in range(0, n-k+1):
            r, rh = cakes[j]
            area = r*r + rh
            dbg_print("....................")
            dbg_print("[{}] r:{} r*h:{}".format(j,r,rh))
            nxtcakes = cakes[j+1:] # next cakes with radius <= r
            dbg_print(nxtcakes)
            nxtcakes.sort(key=itemgetter(1), reverse=True)
            dbg_print(nxtcakes)
            area += sum(pair[1] for pair in nxtcakes[:k-1])
            dbg_print(area)
            if area > sol:
                sol = area
                dbg_print("  -> new best")


        print("Case #{}: {}".format(i, sol*pi))

if __name__ == "__main__":
    main()
