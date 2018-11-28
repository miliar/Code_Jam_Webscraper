fin = open('input', 'r')
fout = open('output', 'w')
for c in range(int(fin.readline())):
    constrains = map(int, fin.readline().split())
    n = constrains[0]
    m = constrains[1]
    current = [[100 for _ in range(m)] for _ in range(n)]
    goal = [[] for _ in range(n)]
    for i in range(n):
        goal[i] = map(int, fin.readline().split())
    for i in range(n):
        max_elem = max(goal[i])
        for j in range(m):
            current[i][j] = min(current[i][j], max_elem)
    for j in range(m):
        max_elem = 0
        for i in range(n):
            max_elem = max(max_elem, goal[i][j])
        for i in range(n):
            current[i][j] = min(current[i][j], max_elem)

    fout.write("Case #{0}: {1}\n".format(c + 1, 'YES' if (goal == current) else 'NO'))
