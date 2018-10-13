debug = False

def dbg_print(x):
    if debug:
        print(x)

def next_color(r, y, b, prev, init):
    if r == 1 and y == 1 and b == 1:
        if prev == "R":
            if init == "R":
                return ("YRB", 0, 0, 0)
            if init == "Y":
                return ("YRB", 0, 0, 0)
            if init == "B":
                return ("BRY", 0, 0, 0)
        if prev == "Y":
            if init == "R":
                return ("RYB", 0, 0, 0)
            if init == "Y":
                return ("RYB", 0, 0, 0)
            if init == "B":
                return ("BYR", 0, 0, 0)
        if prev == "B":
            if init == "R":
                return ("RBY", 0, 0, 0)
            if init == "Y":
                return ("YBR", 0, 0, 0)
            if init == "B":
                return ("RBY", 0, 0, 0)

    if prev == "R":
        if y > 0 and y >= b:
            return ("Y", r, y-1, b)
        elif b > 0:
            return ("B", r, y, b-1)
        else:
            return ("IMPOSSIBLE", r, y, b)

    if prev == "Y":
        if r > 0 and r >= b:
            return ("R", r-1, y, b)
        elif b > 0:
            return ("B", r, y, b-1)
        else:
            return ("IMPOSSIBLE", r, y, b)

    if prev == "B":
        if r > 0 and r >= y:
            return ("R", r-1, y, b)
        elif y > 0:
            return ("Y", r, y-1, b)
        else:
            return ("IMPOSSIBLE", r, y, b)

    # only first char
    if prev == "":
        if r > 0 and r >= y and r >= b:
            return ("R", r-1, y, b)
        elif y > 0 and y >= b:
            return ("Y", r, y-1, b)
        elif b > 0:
            return ("B", r, y, b-1)
        else:
            return ("IMPOSSIBLE", r, y, b)

def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, r, o, y, g, b, v = [int(s) for s in input().split(" ")]
        org = (r,y,b)
        sol = ""
        c   = ""
        fst = ""
        while r + y + b > 0:
            c, r, y, b = next_color(r, y, b, c, fst)
            dbg_print("'{}' next:{} r:{} y:{} b:{}".format(sol,c,r,y,b))
            if fst == "":
                fst = c
            if c == "IMPOSSIBLE":
                sol = "IMPOSSIBLE"
                break
            sol = sol + c

        if sol[0] == sol[-1]:
            sol = "IMPOSSIBLE"

        print("Case #{}: {}".format(i, sol))

if __name__ == "__main__":
    main()
