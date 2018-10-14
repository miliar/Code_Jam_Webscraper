import sys

with open(sys.argv[1]) as f:
    looper = int(f.readline())
    case = 0
    while looper > 0:
        case +=1
        looper -= 1
        matrix = {}
        matrix[0] = [x for x in filter(lambda g: g != '\n', f.readline())]
        matrix[1] = [x for x in filter(lambda g: g != '\n', f.readline())]
        matrix[2] = [x for x in filter(lambda g: g != '\n', f.readline())]
        matrix[3] = [x for x in filter(lambda g: g != '\n', f.readline())]
        f.readline()

        row_results = [set(x) for x in matrix.values()]
        
        if set(['X']) in row_results or set(['X', 'T']) in row_results:
            print 'Case #{0}: X won'.format(case)
            continue
        elif set(['O']) in row_results or set(['O', 'T']) in row_results:
            print 'Case #{0}: O won'.format(case)
            continue

        diagnol = []
        diagnol.append(set([matrix[0][0],
                            matrix[1][1],
                            matrix[2][2],
                            matrix[3][3],
                            ]))
        diagnol.append(set([matrix[0][3],
                            matrix[1][2],
                            matrix[2][1],
                            matrix[3][0],
                            ]))

        if set(['X']) in diagnol or set(['X', 'T']) in diagnol:
            print 'Case #{0}: X won'.format(case)
            continue
        elif set(['O']) in diagnol or set(['O', 'T']) in diagnol:
            print 'Case #{0}: O won'.format(case)
            continue

        column_results = []
        column_results.append(set([matrix[0][0],
                                   matrix[1][0],
                                   matrix[2][0],
                                   matrix[3][0],
                                  ]))
        column_results.append(set([matrix[0][1],
                                   matrix[1][1],
                                   matrix[2][1],
                                   matrix[3][1],
                                  ]))
        column_results.append(set([matrix[0][2],
                                   matrix[1][2],
                                   matrix[2][2],
                                   matrix[3][2],
                                  ]))
        column_results.append(set([matrix[0][3],
                                   matrix[1][3],
                                   matrix[2][3],
                                   matrix[3][3],
                                  ]))

        if set(['X']) in column_results or set(['X', 'T']) in column_results:
            print 'Case #{0}: X won'.format(case)
            continue
        elif set(['O']) in column_results or set(['O', 'T']) in column_results:
            print 'Case #{0}: O won'.format(case)
            continue

        check_for_empty = set()
        map(lambda row: check_for_empty.update(row), row_results)
        if '.' in check_for_empty:
            print 'Case #{0}: Game has not completed'.format(case)
        else:
            print 'Case #{0}: Draw'.format(case)