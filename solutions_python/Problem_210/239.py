debug = False

def dbg_print(x):
    if debug:
        print(x)

def solve(act):
    s0, e0 = act[0]
    s1, e1 = act[1]

    if e1 - s0 > 0 and e1 - s0 <= 720:
        return(2)
    if e0 - s1 > 0 and e0 - s1 <= 720:
        return(2)

    if 24*60 + e1 - s0 > 0 and 24*60 + e1 - s0 <= 720:
        return(2)
    if 24*60 + e0 - s1 > 0 and 24*60 + e0 - s1 <= 720:
        return(2)

    return(4)

def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        ac, aj = [int(s) for s in input().split(" ")]
        act = []
        for j in range(0, ac + aj):
            s, e = [int(s) for s in input().split(" ")]
            act.append( (s,e) )


def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        ac, aj = [int(s) for s in input().split(" ")]
        act = []
        for j in range(0, ac + aj):
            s, e = [int(s) for s in input().split(" ")]
            act.append( (s,e) )

        if ac == 2 or aj == 2:
            nb = solve(act)
        else:
            nb = 2

        print("Case #{}: {}".format(i, nb))

if __name__ == "__main__":
    main()
