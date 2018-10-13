T = int(raw_input().strip())

for t in range(T):
    R, C = [int(item) for item in raw_input().strip().split()]
    matrix = list()
    for i in range(R):
        matrix.append(list(raw_input().strip()))
    for row in matrix:
        i = 0
        base_c = None
        while i < len(row):
            c = row[i]
            if c == '?' and base_c is not None:
                row[i] = base_c
            elif c != '?' and base_c is None:
                base_c = c
                i = 0
                continue
            elif c != '?' and base_c is not None:
                base_c = c
            i += 1

    j = 0
    while j < C:
        i = 0
        base_c = None
        while i < R:
            c = matrix[i][j]
            if c == '?' and base_c is not None:
                matrix[i][j] = base_c
            elif c != '?' and base_c is None:
                base_c = c
                i = 0
                continue
            elif c != '?' and base_c is not None:
                base_c = c
            i += 1
        j += 1

    print('Case #%d:' % (t +1,))
    for row in matrix:
        s = ''
        for c in row:
            s += c
        print(s)
