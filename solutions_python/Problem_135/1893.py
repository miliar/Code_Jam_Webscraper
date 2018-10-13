def solve():

    N = 4

    def f():
        ret = None
        choice = int(raw_input())
        for i in range(N):
            row = [int(x) for x in raw_input().split()]
            if i == choice - 1:
                ret = row
        return set(ret)

    r1 = f()
    r2 = f()
    return r1 & r2
            


if __name__ == '__main__':
    tc = int(raw_input())
    for cc in range(tc):
        a = solve()
        buff = "Case #%d: " % (cc + 1)
        if len(a) == 1:
            for i in a:
                buff += str(i)
        elif len(a) > 1:
            buff += "Bad magician!"
        else:
            buff += "Volunteer cheated!"
        print buff
