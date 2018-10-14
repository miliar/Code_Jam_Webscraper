# 0th solution to Problem B
IMP = "IMPOSSIBLE"

t = int(input())


# RY = O
# BY = G
# RB = V

def solve():
    N, R, RY, Y, BY, B, RB = map(int, input().split(' '))
    if R <= B + Y and B <= R + Y and Y <= B + R:
        x, y, z = None, None, None
        m = {"R": R, "Y": Y, "B": B}
        if R >= B and B >= Y:
            x = "R"
            y = "B"
            z = "Y"
        elif R >= Y and Y >= B:
            x = "R"
            y = "Y"
            z = "B"
        elif B >= Y and Y >= R:
            x = "B"
            y = "Y"
            z = "R"
        elif B >= R and R >= Y:
            x = "B"
            y = "R"
            z = "Y"
        elif Y >= B and B >= R:
            x = "Y"
            y = "B"
            z = "R"
        elif Y >= R and R >= B:
            x = "Y"
            y = "R"
            z = "B"
        res = ""
        res = (y+z)*m[z] + (y+x)*(m[y]-m[z])
        i = 1
        for a1 in range(m[x]-m[y]+m[z]):
            res = res[:i] + x + res[i:]
            i += 2
        return res
    else:
        return IMP



for a0 in range(t):
    sol = solve()
    print("Case #" + str(a0 + 1) + ": " + sol)
