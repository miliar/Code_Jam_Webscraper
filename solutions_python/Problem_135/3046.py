import sys


def read_matrix(f):
    matrix = []
    for i in xrange(4):
        line = f.readline()
        matrix.append([int(num) for num in line.split(' ')])

    return matrix

def generate_solution(matrix1, matrix2, i1, i2):

    l1 = matrix1[i1 - 1]
    l2 = matrix2[i2 - 1]

    matching = []

    for j in l1:
        for k in l2:
            if j == k:
                matching.append(k)

    if len(matching) == 0:
        return 'Volunteer cheated!'
    elif len(matching) == 1:
        return matching[0]
    else:
        return 'Bad magician!'

def main(input_path):

    f = open(input_path, 'rb')
    solution = open('solution.out', 'wb')
    test_cases = int(f.readline())

    for i in xrange(test_cases):
        i1 = int(f.readline())
        matrix1 = read_matrix(f)
        i2 = int(f.readline())
        matrix2 = read_matrix(f)
        sol_str = generate_solution(matrix1, matrix2, i1, i2)
        solution.write('Case #{}: {}\n'.format(i + 1, sol_str))


    f.close()
    solution.close()

if __name__ == "__main__":
    main(sys.argv[1])