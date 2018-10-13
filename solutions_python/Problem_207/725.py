T = int(raw_input())
for t in xrange(1, T + 1):
    n, r, o, y, g, b, v = map(int, raw_input().split())
    sol = ""
    if r == y and y == b:
        sol = "RYB" * r
    else:
        mxx = max(r, y, b)
        if r == mxx and y + b >= r:
            turn = True if max(y, b) == y else False
            while r > 0:
                r -= 1
                if turn and y > 0:
                    sol += "RY"
                    y -= 1
                elif not turn and b > 0:
                    sol += "RB"
                    b -= 1

                if y == 0:
                    turn = False
                elif b == 0:
                    turn = True
                else:
                    turn = not turn
            while y > 0 or b > 0:
                temp = ""
                while sol:
                    if sol[1] == "Y" and b > 0:
                        b -= 1
                        temp += sol[:2] + "B"
                        sol = sol[2:]
                    elif sol[1] == "B" and y > 0:
                        y -= 1
                        temp += sol[:2] + "Y"
                        sol = sol[2:]
                    elif sol[1] == "Y" and b == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                    elif sol[1] == "B" and y == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                sol = temp
        elif y == mxx and r + b >= y:
            turn = True if max(r, b) == r else False
            while y > 0:
                y -= 1
                if turn and r > 0:
                    sol += "YR"
                    r -= 1
                elif not turn and b > 0:
                    sol += "YB"
                    b -= 1

                if r == 0:
                    turn = False
                elif b == 0:
                    turn = True
                else:
                    turn = not turn
            while r > 0 or b > 0:
                temp = ""
                while sol:
                    if sol[1] == "R" and b > 0:
                        b -= 1
                        temp += sol[:2] + "B"
                        sol = sol[2:]
                    elif sol[1] == "B" and r > 0:
                        r -= 1
                        temp += sol[:2] + "R"
                        sol = sol[2:]
                    elif sol[1] == "R" and b == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                    elif sol[1] == "B" and r == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                sol = temp
        elif b == mxx and y + r >= b:
            turn = True if max(y, r) == y else False
            while b > 0:
                b -= 1
                if turn and y > 0:
                    sol += "BY"
                    y -= 1
                elif not turn and r > 0:
                    sol += "BR"
                    r -= 1

                if y == 0:
                    turn = False
                elif r == 0:
                    turn = True
                else:
                    turn = not turn
            while y > 0 or r > 0:
                temp = ""
                while sol:
                    if sol[1] == "Y" and r > 0:
                        r -= 1
                        temp += sol[:2] + "R"
                        sol = sol[2:]
                    elif sol[1] == "R" and y > 0:
                        y -= 1
                        temp += sol[:2] + "Y"
                        sol = sol[2:]
                    elif sol[1] == "Y" and r == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                    elif sol[1] == "R" and y == 0:
                        temp += sol[:2]
                        sol = sol[2:]
                sol = temp

    if sol:
        print 'Case #{0}: {1}'.format(t, sol)
    else:
        print 'Case #{0}: IMPOSSIBLE'.format(t)
