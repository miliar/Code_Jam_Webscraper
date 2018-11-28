
import os
import sys


def cases():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    lines = lines[1:]

    while lines:
        r, c = map(int, lines.pop(0).split())
        case_lines = lines[:r]
        data = [list(row.strip()) for row in lines[:r]]
        lines = lines[r:]
        yield data


def hasq(data):
    return '?' in ''.join([''.join(row) for row in data])


def allq(row):
    return all(v == '?' for v in row)


def main():
    for case_i, data in enumerate(cases()):

        # Replace out rows where possible
        for i, row in enumerate(data):
            if not allq(row):
                while hasq(row):
                    for j, val in enumerate(row):
                        if val == '?':
                            pv = row[j-1] if j-1 > -1 else None
                            nv = row[j+1] if j+1 < len(row) else None
                            if pv is not None and pv != '?':
                                row[j] = pv
                            elif nv is not None and nv != '?':
                                row[j] = nv

        while hasq(data):
            for i, row in enumerate(data):
                if allq(row):
                    for j, val in enumerate(row):
                        pv = data[i-1][j] if i-1 > -1 else None
                        nv = data[i+1][j] if i+1 < len(data) else None
                        if pv is not None and pv != '?':
                            row[j] = pv
                        elif nv is not None and nv != '?':
                            row[j] = nv

        print 'Case #{}:'.format(case_i + 1)
        print '\n'.join([''.join(row) for row in data])



if __name__ == '__main__':
    main()
