# pylint: disable=missing-docstring
import sys


class Group:
    def __init__(self, workers, machines):
        self.workers = workers
        self.machines = machines


def problem(matrix):
    size = len(matrix)
    present = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j]:
                present += 1

    groups = []
    for worker in range(size):
        workermachines = set()
        for i, b in enumerate(matrix[worker]):
            if b:
                workermachines.add(i)
        found = []
        for group in groups:
            if group.machines & workermachines:
                found.append(group)
        new_workers = [worker]
        for x in found:
            groups.remove(x)
            new_workers += x.workers
            workermachines |= x.machines
        groups.append(Group(new_workers, workermachines))

    missing = set(range(size))
    for group in groups:
        missing -= group.machines

    foo = []

    for n in groups:
        foo.append((len(n.workers), len(n.machines)))
    for n in missing:
        foo.append((0, 1))

    if len(foo) == size * 2:
        return size
    res = find_best(foo)

    return res - present


def find_best(foo):
    s = 0
    for x in foo:
        s += x[0] * x[1]
        if x[0] != x[1]:
            break
    else:
        return s
    best = -1
    for a in foo:
        for b in foo:
            if a != b:
                new_list = foo[:]
                new_list.remove(a)
                new_list.remove(b)
                new_list.append((a[0] + b[0], a[1] + b[1]))
                new = find_best(new_list)
                if new < best or best == -1:
                    best = new
    return best







def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            number = int(nextline(infile))
            matrix = []
            for i in range(number):
                matrix.append([(x == '1') for x in nextline(infile)])
            result += 'Case #{}: {}\n'.format(1 + run, problem(matrix))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
