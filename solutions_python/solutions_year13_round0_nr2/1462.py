import sys

with open(sys.argv[1]) as f:
    looper = int(f.readline())
    case = 0
    while looper > 0:
        case +=1
        looper -= 1

        n, m = [int(x) for x in filter(lambda g: g != '\n', f.readline()).split(' ')]

        line = 0
        lawn = {}
        while line < n:
            lawn[line] = [int(x) for x in filter(lambda g: g != '\n', f.readline()).split(' ')]
            line += 1

        can_be_done = True
        line = 0
        while line < n and can_be_done:
            minimum = min(lawn[line])
            if set(lawn[line]) != set([minimum]):
                min_match_index = set()
                walk = 0
                for h in lawn[line]:
                    if h == minimum:
                        min_match_index.add(walk)
                    walk += 1

                for min_idx in min_match_index:
                    column = []
                    for jdx in range(n):
                        column.append(lawn[jdx][min_idx])
                    max_column = max(column)
                    if minimum != max_column:
                        can_be_done = False
                        break
                        
            line += 1
        if can_be_done:
            print 'Case #{0}: YES'.format(case)
        else:
            print 'Case #{0}: NO'.format(case)