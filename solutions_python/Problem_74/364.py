import sys

def solve(line):
    seq = line.split()
    n = int(seq[0])
    col = ['O', 'B']
    pos = [1, 1]
    ind = 1
    while ind < len(seq):
        col.append(seq[ind])
        pos.append(int(seq[ind+1]))
        ind += 2

    succ = [-1 for _ in col]
    last = -1
    for ind in range(len(pos))[::-1]:
        if col[ind] == 'O':
            succ[ind] = last
            last = ind

    last = -1
    for ind in range(len(pos))[::-1]:
        if col[ind] == 'B':
            succ[ind] = last
            last = ind

    o_pos = 0
    b_pos = 1
    o_dist = abs(pos[o_pos] - pos[succ[o_pos]])
    b_dist = abs(pos[b_pos] - pos[succ[b_pos]])
    ret = 0
    ind = 2

#    print col
#    print pos
#    print succ

    while ind < len(pos):
        if col[ind] == 'O':
            ret += o_dist + 1
            b_dist -= (o_dist + 1)
            if b_dist < 0:
                b_dist = 0
            o_pos = succ[o_pos]
            o_dist = abs(pos[o_pos] - pos[succ[o_pos]])
        else:
            ret += b_dist + 1
            o_dist -= (b_dist + 1)
            if o_dist < 0:
                o_dist = 0
            b_pos = succ[b_pos]
            b_dist = abs(pos[b_pos] - pos[succ[b_pos]])

        ind += 1

    return ret


def main():
    if len(sys.argv) != 2:
        raise ValueError
    filename = sys.argv[1]
    file = open(filename, 'r')
    n_tests = int(file.readline())
    for test in range(1, n_tests + 1):
        answer = solve(file.readline())
        print "Case #{0}: {1}".format(test, answer)

main()
