if __name__ == "__main__":
    RICHARD = 'RICHARD'
    GABRIEL = 'GABRIEL'
    t = int(input())
    for case in range(t):
        x, r, c = [int(x) for x in input().split()]
        if r < c:
            r, c = c, r
        if r == 1:
            if x == 1:
                res = GABRIEL
            else:
                res = RICHARD
        elif r == 2:
            if x <= 2:
                res = GABRIEL
            else:
                res = RICHARD
        elif r == 3:
            if c == 1:
                if x == 1:
                    res = GABRIEL
                else:
                    res = RICHARD
            elif c == 2:
                if x <= 3:
                    res = GABRIEL
                else:
                    res = RICHARD
            else:
                # c == 3
                if x == 1 or x == 3:
                    res = GABRIEL
                else:
                    res = RICHARD
        elif r == 4:
            if c == 1:
                if x <= 2:
                    res = GABRIEL
                else:
                    res = RICHARD
            if c == 2:
                if x <= 2:
                    res = GABRIEL
                else:
                    res = RICHARD
            if c == 3:
                res = GABRIEL
            if c == 4:
                if x != 3:
                    res = GABRIEL
                else:
                    res = RICHARD

        print("Case #{0}: {1}".format(case+1, res))