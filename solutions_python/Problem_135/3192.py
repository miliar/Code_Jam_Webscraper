def is_possible(matrix1, row1, matrix2, row2):
    set1 = set(matrix1[row1])
    set2 = set(matrix2[row2])

    intersection = set1.intersection(set2)

    if len(intersection) == 0:
        return "Volunteer cheated!"
    elif len(intersection) == 1:
        return [x for x in intersection][0]
    else:
        return "Bad Magician!"


def read_test(f):
    answer = int(f.readline())
    matrix = []
    for i in range(4):
        raw_row = f.readline()
        row = [int(x) for x in raw_row.split()]
        matrix.append(row)
    return answer, matrix


def main(file_path):
    f = open(file_path, 'r')
    test_cases = int(f.readline())

    for i in range(test_cases):
        a1, m1 = read_test(f)
        a2, m2 = read_test(f)
        result = is_possible(m1, a1 - 1, m2, a2 - 1)
        print "Case #{0}: {1}".format(i + 1, result)


if __name__ == "__main__":
    import sys
    f_name = sys.argv[1]
    main(f_name)
