from sys import stdin

file = stdin
def read_line():
    return file.readline()

def read_int():
    return int(read_line())

def get_matrix():
    matrix = []
    for i in range(4):
        matrix.append(set(map(lambda y: int(y), read_line().split())))
    return matrix

def outcome(set1, set2):
    overlap = set1.intersection(set2)
    if len(overlap) == 1:
        return list(overlap)[0]
    elif len(overlap) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

cases = int(read_line())
for case_no in range(1, cases + 1):
    row1 = read_int()
    set1 = get_matrix()[row1 - 1]
    row2 = read_int()
    set2 = get_matrix()[row2 - 1]
    print("Case #{0}: {1}".format(case_no, outcome(set1, set2)))