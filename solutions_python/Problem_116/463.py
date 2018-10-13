# python 2.7
# Problem A: Tic-Tac-Toe-Tomek

def t4_isWinner(m, p):
    m = [tuple(row.replace("T", p)) for row in m]
    s = tuple(p * 4)

    if s in m or s in zip(*m):
        return True # finally!
    return s == tuple(m[i][i] for i in (0,1,2,3)) \
        or s == tuple(m[i][3-i] for i in (0,1,2,3))

def t4_getWinnerString(m):
    o = t4_isWinner(m, "O")
    x = t4_isWinner(m, "X")
    if o and x: return "Draw"
    if o: return "O won"
    if x: return "X won"
    for row in m:
        if "." in row: return "Game has not completed"
    return "Draw"

def answer(case, s):
    return "Case #%d: %s"%(case, s)

if __name__ == "__main__":

    def parse_run(s):
        lines = s.split("\n")
        count = int(lines[0])

        for i in range(count):
            j = 1 + 5 * i
            m = lines[j:j + 4]
            print answer(i + 1, t4_getWinnerString(m))

    import sys
    try: fn = sys.argv[1]
    except IndexError: fn = "A-large.in" # oops, had wrong name here for small

    with file(fn) as fp:
        parse_run(fp.read())

