import sys
from collections import defaultdict

def check_cake_face(face, flip_counts):
    if flip_counts % 2 == 0:
        return face
    elif face == '+':
        return '-'
    else:
        return '+'

def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        cakes_row, f_size = content[i].split(' ')
        f_size = int(f_size)
        done = False
        cake_n = 0
        flips = defaultdict(int)
        n_flips = 0
        cakes_num = len(cakes_row)
        while cake_n + f_size < cakes_num:
            if check_cake_face(cakes_row[cake_n], flips[cake_n]) != '+':
                for j in range(cake_n, cake_n + f_size):
                    flips[j] += 1
                n_flips += 1
            cake_n += 1

        last_cakes = set([check_cake_face(c, flips[ind]) for c, ind in zip(cakes_row[-f_size:], range(cakes_num - f_size, cakes_num))])
        if len(last_cakes) == 2:
            r = 'IMPOSSIBLE'
        else:
            r = n_flips 
            if last_cakes.pop() == '-':
                r += 1

        print("Case #%s: %s" % (i, r))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
