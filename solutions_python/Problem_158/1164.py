
def read_ints(): return map(int, input().strip().split())

GABRIEL, RICHARD = "GABRIEL", "RICHARD"


def test(x, r, c):
    r, c = sorted([r, c])
    if (r * c) % x != 0:
        return RICHARD

    if x == 1:
        return GABRIEL
    if x == 2:
        return GABRIEL
    if x == 3:
        if (r, c) == (1, 3):
            return RICHARD
        else:
            return GABRIEL
        
    if x == 4:
        if (r, c) in [(4, 4), (3, 4)]:
            return GABRIEL
        else:
            return RICHARD

t, = read_ints()
for tc in range(t):
    input_data = read_ints()
    ans = test(*input_data)
    print("Case #{}: {}".format(tc + 1, ans))
