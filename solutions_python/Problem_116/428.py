import sys

def read_int():
    return int(gets())

def gets():
    return sys.stdin.readline().rstrip('\r\n')

def test(p1, p2, p3, p4):
    for p in (p1,p2,p3,p4):
        if p == '.':
            return None

    sign = None
    for p in (p1,p2,p3,p4):
        if p != 'T':
            sign = p
            break
    
    for p in (p1,p2,p3,p4):
        if p == 'T':
            continue
        elif p == sign:
            continue
        else:
            return None
    
    return "%s won" % (sign)


def solve(s):
    for r in range(4):
        test_result = test(s[r][0], s[r][1], s[r][2], s[r][3])
        if test_result != None:
            return test_result
    for c in range(4):
        test_result = test(s[0][c], s[1][c], s[2][c], s[3][c])
        if test_result != None:
            return test_result
    test_result = test(s[0][0], s[1][1], s[2][2], s[3][3])
    if test_result != None:
        return test_result
    test_result = test(s[0][3], s[1][2], s[2][1], s[3][0])
    if test_result != None:
        return test_result

    # Draw or incomplete?
    for i in range(4):
        for j in range(4):
            if s[i][j] == '.':
                return "Game has not completed"
    return "Draw"


t = read_int()
for ti in range(t):
    s = []
    for i in range(4):
        s.append(gets())

    ans = solve(s)
    print("Case #%d: %s" % (ti+1, ans))
    gets()
