#!/usr/bin/python

filename = 'standing-large'
out_case = 1
lines_per_case = 1


def write_out(result):
    global out_case
    with open('{}.out'.format(filename), 'a+') as fout:
        fout.write('Case #{}: {}\n'.format(out_case, result))
        out_case += 1


def solve_case(lines):
    line = lines[0]
    max_s, line = line.split(' ')
    max_s = int(max_s)
    if max_s == 0:
        write_out(0)
        return

    people = 0
    acc = 0
    for i in xrange(max_s + 1):
        n = int(line[i])
        if n == 0:
            if acc <= i:
                people += 1
                n = 1
        acc += n
    write_out(people)

if __name__ == '__main__':
    with open('{}.in'.format(filename)) as fin:
        lines = fin.readline()
        lines_read = 0
        lines_acc = []
        for line in fin:
            lines_acc.append(line.strip())
            lines_read += 1
            if lines_read == lines_per_case:
                solve_case(lines_acc)
                lines_acc = []
                lines_read = 0