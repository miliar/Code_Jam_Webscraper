'''rubber-stamp solution'''
from copy import deepcopy


def can_cut(line, height):
    return (max(line) == height and
            # there is no other heights except for zero
            not filter(lambda x: x and x != height, line))


def get_sorted_heights(matrix):
    unique = set()
    for row in matrix:
        for elem in row:
            unique.update([elem])
    return sorted(unique)


def process_case(n, m, matrix):
    for height in get_sorted_heights(matrix):
        cut_matrix = deepcopy(matrix)
        for i, row in enumerate(matrix):
            if can_cut(row, height):
                cut_matrix[i] = [0]*m
        for j, col in enumerate(zip(*matrix)):
            if can_cut(col, height):
                for i in range(n):
                    cut_matrix[i][j] = 0
        matrix = deepcopy(cut_matrix)
    for row in matrix:
        for elem in row:
            if elem != 0:
                return "NO"
    return "YES"

def read_input():
    n, m = map(int, raw_input().split())
    matrix = []
    for _ in range(n):
        matrix.append(map(int, raw_input().split()))
    return n, m, matrix

def process_input():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases + 1):
        n, m, matrix = read_input()
        answer = process_case(n, m, matrix)
        print 'Case #%d: %s' % (case_number, answer)

if __name__ == '__main__':
    process_input()
