#!/usr/bin/env python

def answer(n):
    return str(n/2) + " " + str((n-1)/2)

def Solve(n, k):
    nb = n
    cntb = 1
    cnts = 0

    while True:
        if k <= cntb:
            return answer(nb)
        if k <= cnts+cntb:
            return answer(nb-1)
        k -= cntb+cnts
        if (nb&1) == 1:
            cntb, cnts = cntb*2 + cnts, cnts
            nb = nb/2
        else:
            cntb, cnts = cntb, cntb + cnts*2
            nb = nb/2
    return ""

def main():
    with open("c.txt") as _in, open("c_out.txt", "w") as _out:
        i = -1
        for line in _in:
            i += 1
            if i == 0:
                continue
            parts = line.split(" ")
            n, k  = int(parts[0]), int(parts[1])
            res = Solve(n, k)
            _out.write("Case #" + str(i) + ": " + res + "\n")



if __name__ == "__main__":
    main()
