import sys

inp = sys.stdin.read().split("\n")
cases = int(inp.pop(0))

for case in range(cases):
    start = int(inp.pop(0))
    startboard = [[int(i) for i in inp.pop(0).split()] for _ in range(4)]

    end = int(inp.pop(0))
    endboard = [[int(i) for i in inp.pop(0).split()] for _ in range(4)]

    similar = set(startboard[start-1]) & set(endboard[end-1])
    if not similar:
        print("Case #%d: Volunteer cheated!" % (case + 1))
    elif len(similar) == 1:
        print("Case #%d: %d" % (case + 1, similar.pop()))
    else:
        print("Case #%d: Bad magician!" % (case + 1))

