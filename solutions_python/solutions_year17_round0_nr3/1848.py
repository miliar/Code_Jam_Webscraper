import os
from bintrees import bintree


def read_file(filename):
    path = os.path.join('inputs', filename)
    with open(path, 'r') as f:
        return f.readlines()


def write_file(filename, content):
    path = os.path.join('outputs', filename + '.out')
    with open(path, 'w+') as f:
        return f.writelines(content)


def main():
    for in_file in os.listdir('inputs'):
    # for in_file in ['test.in']:
        content = read_file(in_file)
        result = algo(content)
        write_file(in_file, result)


def algo(content):
    size = int(content[0])
    inputs = [map(int, line.strip().split()) for line in content[1:1+size]]

    return [format_(i, x) for i, x in enumerate([solution(*line) for line in inputs])]


def solution(size, persons):
    print ("================================" * 2)
    sizes = {size: 1}
    while persons > 0:
        print (str(persons) + " persons", sizes)
        n, max_ = get_max(sizes)
        print ("max {}   {} times".format(max_, n))
        new_spaces = split_space(max_)
        insert_new_spaces(sizes, new_spaces, n)
        persons -= n
    return format_spaces(new_spaces)


def get_max(tree):
    max_ = max(tree)
    n = tree[max_]
    del tree[max_]
    return n, max_


def insert_new_spaces(tree, spaces, m):
    for space in spaces:
        n = tree.get(space)
        if not n:
            tree[space] = m
        else:
            tree[space] += m


def split_space(space):
    if space % 2 == 1:
        return [int(space / 2), int(space / 2)]
    else:
        return [int(space / 2), int(space / 2) - 1]

def format_spaces(spaces):
    if len(spaces) == 0:
        left, right = 0, 0
    elif len(spaces) == 1:
        left, right = 1, 0
    else:
        left, right = spaces
    return "{} {}".format(max(left, right), min(left, right))


def format_(i, x):
    return "Case #{}: {}\n".format(i + 1, x)

if __name__ == '__main__':
    main()
