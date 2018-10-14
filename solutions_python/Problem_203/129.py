lines = []
with open("A-large.in", 'r') as reader:
   lines = reader.readlines()
t = int(lines[0])
lines = iter(lines[1:])
out = open("1.out", 'w')

for i in range(t):
    tokens = next(lines).split()
    grid = []
    empty = set()
    for j in range(int(tokens[0])):
        line = next(lines)
        grid += [[False if x == '?' else x for x in line.strip()]]
    for j in range(int(tokens[0])):
        if not any(grid[j]):
            empty.add(j)
            continue
        for k in range(int(tokens[1])):
            if grid[j][k]:
                curr = grid[j][k]
                break
        for k in range(int(tokens[1])):
            if not grid[j][k]:
                grid[j][k] = curr
            else:
                curr = grid[j][k]
    for j in range(int(tokens[0])):
        if j not in empty:
            curr = j
            break
    for j in range(int(tokens[0])):
        if j in empty:
            grid[j] = grid[curr]
        else:
            curr = j
    out.write("Case #" + str(i + 1) + ':\n')
    for j in range(int(tokens[0])):
        out.write(''.join(grid[j]) + '\n')

