#! /usr/bin/env python3

def main():
    with open("2017.0A0.txt") as f:
        t = int(f.readline())
        for i in range(t):
            sol = calc_flips(f.readline())
            print("Case #%d: %s" % (i + 1, sol))

def calc_flips(l):
    k = int(l.split()[1])
    pans = list(map(lambda pan: True if pan == "+" else False, l.split()[0]))
    flips = 0
    while len(pans) > k:
        if not pans[0]:
            flips += 1
            pans = list(map(lambda pan:not pan, pans[:k])) + pans[k:]
        pans = pans[1:]
    if all(pans):
        return flips
    elif all(map(lambda pan:not pan, pans)):
        return flips + 1
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    main()
