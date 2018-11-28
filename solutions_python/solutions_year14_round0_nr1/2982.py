try: input = raw_input
except NameError: pass

for t in range(1, int(input()) + 1):
    first_i = int(input()) - 1
    first_row = set(int(i) for i in
                    [input(), input(), input(), input()][first_i].split())
    second_i = int(input()) - 1
    second_row = set(int(i) for i in
                        [input(), input(), input(), input()][second_i].split())
    candidates = first_row.intersection(second_row)
    length = len(candidates)
    fmt_str = 'Case #' + str(t) + ': {}'
    if length == 0:
        print fmt_str.format('Volunteer cheated!')
    elif length == 1:
        print fmt_str.format(candidates.pop())
    else:
        print fmt_str.format('Bad magician!')
