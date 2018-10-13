#!/usr/bin/python
#

def pop_from_list(li):
    if len(li) == 0:
        return None
    return li.pop(0)

def parse(line):

    tokens = line.split()

    position_order = {}
    position_order['O'] = []
    position_order['B'] = []

    color_order = []

    N = int(tokens[0])
    for i in range(N):
        color = tokens[i*2+1]
        position = int(tokens[i*2+2])
        position_order[color].append(position)
        color_order.append(color)

    return (color_order, position_order)

def run(color_order, position_order):

    if len(color_order) == 0:
        return 0

    B_order = position_order['B']
    O_order = position_order['O']

    time = 1
    b_pos = 1
    o_pos = 1
    b_exp_pos = pop_from_list(B_order)
    o_exp_pos = pop_from_list(O_order)
    next_color = pop_from_list(color_order)
    pushed = False

    while True:
        if pushed:
            if next_color == 'B':
                b_exp_pos = pop_from_list(B_order)
            else:
                o_exp_pos = pop_from_list(O_order)
            next_color = pop_from_list(color_order)
            pushed = False

        if b_exp_pos == None:
            pass
        elif b_pos < b_exp_pos:
            b_pos = b_pos + 1
        elif b_pos > b_exp_pos:
            b_pos = b_pos - 1
        elif next_color == 'B':
            pushed = True

        if o_exp_pos == None:
            pass
        elif o_pos < o_exp_pos:
            o_pos = o_pos + 1
        elif o_pos > o_exp_pos:
            o_pos = o_pos - 1
        elif next_color == 'O':
            pushed = True

        if pushed and len(color_order) == 0:
            return time

        time = time + 1


if __name__ == "__main__":
    lines = file('A-large.in.txt').read().splitlines()[1:]
    for idx, line in enumerate(lines, start=1):
        color_order, position_order = parse(line)
        time = run(color_order, position_order)

        print "Case #%d: %d" % (idx, time)

