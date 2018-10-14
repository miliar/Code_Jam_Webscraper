cases = input()
for case in xrange(1, cases + 1):
    R, C = map(int, raw_input().split())
    cake = [raw_input() for row in xrange(R)]

    empty_line = '?' * C

    non_empty_lines = [line for line in cake if line != empty_line]
    current_non_empty = non_empty_lines[0]

    for row in xrange(R):
        line = cake[row]
        if line == empty_line:
            cake[row] = current_non_empty
        else:
            current_non_empty = line

    for row in xrange(R):
        line = cake[row]
        current_initial = line.lstrip('?')[0]
        line_list = list(line)

        for j in xrange(C):
            if line[j] == '?':
                line_list[j] = current_initial
            else:
                current_initial = line[j]
        cake[row] = str.join('', line_list)

    print 'Case #%d:' % (case)
    for line in cake:
        print line
