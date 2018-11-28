
import sys


CHECK = ['RG', 'GR', 'VY', 'YV', 'OB', 'BO', 'RY', 'YR', 'YB', 'BY',
         'RB', 'BR']


# def solve(N, R, O, Y, G, B, V):
#     a0 = R - G
#     a1 = R - 2*G
#     b = Y - V
#     c = B - O



def solve(N, R, O, Y, G, B, V):
    a = R - G
    b = Y - V
    c = B - O
    if a < 0 or b < 0 or c < 0 or a+b+c < 2*max(a, b, c):
        return "IMPOSSIBLE"

    A1 = []
    B1 = []
    C1 = []
    for _ in range(G):
        A1.append("RGR")
    for _ in range(R-2*G):
        A1.append("R")

    for _ in range(V):
        B1.append("YVY")
    for _ in range(Y-2*V):
        B1.append("Y")

    for _ in range(O):
        C1.append("BOB")
    for _ in range(B-2*O):
        C1.append("B")
    print A1, B1, C1, a, b, c

    if b > a and b > c:
        A1, B1 = B1, A1
        a, b = b, a
    elif c > a and c > b:
        A1, C1 = C1, A1
        a, c = c, a

    print A1, B1, C1
    ans = ""
    for i in range(a):
        print i, a-c, a-c + b+c-a
        if i < a - c:
            s = B1.pop(0)
        elif i < a-c + b+c-a:
            s = B1.pop(0) + C1.pop(0)
        else:
            s = C1.pop(0)
        ans += A1.pop(0) + s
    print ans


def solve_small(N, R, O, Y, G, B, V):
    (a, ac), (b, bc), (c, cc) = sorted([(R, 'R'), (B, 'B'), (Y, 'Y')])[::-1]
    if a > b + c:
        return "IMPOSSIBLE"

    # print a, b, c, ac, bc, cc

    ans = ""
    for i in range(a):
        ans += ac
        if i < a - c:
            ans += bc
        elif i < a-c + b+c-a:
            ans += bc + cc
        else:
            ans += cc
    # print ans
    return ans


for tc in range(int(raw_input())):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    ans = solve_small(N, R, O, Y, G, B, V)

    if ans != "IMPOSSIBLE":
        assert len(ans) == N
        for a, b in zip(ans, ans[1:] + ans):
            assert a + b in CHECK
        assert ans.count('R') == R
        assert ans.count('O') == O
        assert ans.count('Y') == Y
        assert ans.count('G') == G
        assert ans.count('B') == B
        assert ans.count('V') == V

    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
