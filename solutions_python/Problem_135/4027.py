#!/usr/bin/python


import sys


def _get_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(x) for x in line.split()])

    return matrix


def _get_result(first_row, second_row):
    result = list(first_row.intersection(second_row))
    if len(result) == 0:
        return "Volunteer cheated!"
    elif len(result) == 1:
        return str(result[0])
    elif len(result) > 1:
        return "Bad magician!"


def get_result(cases, data):
    results = []
    for i in xrange(cases):
        line = i * 10
        first_pick = int(data[line]) - 1
        first_matrix = _get_matrix(data[line+1:line+5])
        second_pick = int(data[line+5]) - 1
        second_matrix = _get_matrix(data[line+6:line+11])

        result = _get_result(set(first_matrix[first_pick]),
                             set(second_matrix[second_pick]))
        results.append("Case #%s: %s" % (i+1, result))

    return results

def main():
    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        data = f.readlines()
    cases = int(data[0])
    results = get_result(cases, data[1:])
    for result in results:
        print result

if __name__ == "__main__":
    main()
