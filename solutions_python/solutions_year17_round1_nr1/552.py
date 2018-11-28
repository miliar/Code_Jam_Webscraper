fin = open('A.in', 'r')
fout = open('A.out', 'w')


def check_cake(t, cake):
    fout.write('Case #' + str(t) + ':\n')
    for row in cake:
        for elt in row:
            assert elt != '?', '{}'.format(cake)
        fout.write(''.join(row) + '\n')


T = int(fin.readline())
for t in range(1, T+1):
    R, C = map(int, fin.readline().split())
    cake = []
    for i in range(R):
        arr = list(fin.readline().replace('\n', ''))
        cake.append(arr)
    # grow horizontally
    for row in cake:
        curr = ''
        start = -1
        run = 0
        if row[0] == '?':
            start = 0
            run += 1
        else:
            curr = row[0]
        for i in range(1, C):
            if row[i] == '?':
                if start == -1:
                    start = i
                    run = 0
                run += 1
            else:
                curr = row[i]
                if start != -1:
                    row[start:start+run] = [curr for i in range(run)]
                    start, run = (-1, 0)
        if start != -1 and curr != '':
            row[start:start+run] = [curr for i in range(run)]
    EMPTY_ROW = ['?' for i in range(C)]
    good_row = []
    if cake[0] != EMPTY_ROW:
        good_row = cake[0]
        start, run = -1, 0
    else:
        start, run = 0, 1
    for i in range(R):
        if cake[i][0] == '?':
            assert cake[i] == EMPTY_ROW
            if start == -1:
                start = i
                run = 0
            run += 1
        else:
            good_row = cake[i]
            if start != -1:
                for j in range(start, start+run):
                    cake[j] = good_row
                start, run = -1, 0
    if start != -1 and good_row != []:
        for j in range(start, start+run):
            cake[j] = good_row
    check_cake(t, cake)
