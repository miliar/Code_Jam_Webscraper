# Parenting Partnering

def solve(cd, jk):
    cd.sort()
    jk.sort()
    if len(cd) == 2:
        if max(cd[1][0] - cd[0][1], 1440 + cd[0][0] - cd[1][1]) < 720:
            return 4
    if len(jk) == 2:
        if max(jk[1][0] - jk[0][1], 1440 + jk[0][0] - jk[1][1]) < 720:
            return 4
    return 2

cases = int(raw_input())
for case in range(1, cases + 1):
    (ai, aj) = map(int, raw_input().split(' '))
    cd = [map(int, raw_input().split(' ')) for i in range(ai)]
    jk = [map(int, raw_input().split(' ')) for i in range(aj)]
    print "Case #" + str(case) + ": " + str(solve(cd, jk))
