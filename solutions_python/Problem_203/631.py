T = int(input())

for case in range(T):
    line = input()
    R = int(line.split(" ")[0])
    C = int(line.split(" ")[1])
    cake = [[0 for x in range(C)] for x in range(R)]
    #current char for row, or first char of the row
    character = ['?' for x in range(R)]
    #lists with row indexes
    emptyRows = []
    filledRows = []
    rows = []
    for r in range(0,R):
        line = input()
        count = 0
        for c in range(0,C):
            cake[r][c] = line[c]
            if cake[r][c] != '?':
                count += 1
                if character[r] == '?':
                    character[r] = cake[r][c]
            else:
                count -= 1
        if count == C:
            filledRows.append(r)
        elif count == -C:
            emptyRows.append(r)
        else:
            rows.append(r)
    #fill non-empty rows
    for r in rows:
        for c in range(C):
            if cake[r][c] == '?':
                cake[r][c] = character[r]
            else:
                character[r] = cake[r][c]
        filledRows.append(r)
    #fill empty rows
    filledRows.sort()
    for r in emptyRows:
        if r < filledRows[0]:
            cake[r] = cake[filledRows[0]]
        else:
            cake[r] = cake[r-1]


    print("Case #{}:".format(case+1))
    for r in cake:
        print(''.join(r))


