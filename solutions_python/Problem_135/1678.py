def solve():
    row = input()
    rows = []
    possib = []
    for i in range(4):
        rows.append(raw_input().split(" "))
    for item in rows[row-1]:
        possib.append(item)
    row = input()
    rows = []
    for i in range(4):
        rows.append(raw_input().split(" "))
    count = 0
    solutions = []
    for item in rows[row-1]:
        if item in possib:
            count += 1
            solutions.append(item)
    if count == 0:
        return "Volunteer cheated!"
    if count == 1:
        return solutions[0]
    return "Bad magician!"


T = input()

for i in range(1,T+1):
    res = solve()
    print "Case #%d: %s" % (i, res)
