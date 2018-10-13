__author__ = 'Bill'

# developed with python3.3 + numpy

import sys, time, numpy

def parse_case(file):
    return map(int, file.readline().split())

def process_case(case):
    r, c, m = case

    mines, scores = construct_board(r,c)
    update_scores(mines, scores)

    if r * c == m:
        return build_output(scores)

    while numpy.sum(mines) > m:
        raw_pos = numpy.where(scores == numpy.sum(mines)-m)
        if len(raw_pos[0]) > 0:
            pos = (raw_pos[0][0], raw_pos[1][0])
        else:
            pos = min_pos(scores)
        clear_mines(mines, pos)
        update_scores(mines, scores)
        #print(pos)
        #print(scores)

    if r * c == m + 1:
        return build_output(scores).replace('.', 'C')
    elif numpy.sum(mines) == m:
        return build_output(scores)
    else:
        return '\nImpossible'

def min_pos(scores):
    nonzero_index = numpy.nonzero(scores)
    result = (nonzero_index[0][0], nonzero_index[1][0])
    for i in range(len(nonzero_index[0])):
        if scores[result] > scores[nonzero_index[0][i], nonzero_index[1][i]]:
            result = (nonzero_index[0][i], nonzero_index[1][i])
    return result

def get_sub_matrix(mines, x, y):
    x1 = max(0, x-1)
    x2 = min(mines.shape[0], x+2)
    y1 = max(0, y-1)
    y2 = min(mines.shape[1], y+2)

    return mines[x1:x2, y1:y2]

def clear_mines(mines, pos):
    sm = get_sub_matrix(mines, pos[0], pos[1])
    sm[sm!=0] = 0

def construct_board(r, c):
    mines = numpy.ones([r, c], dtype=int)
    scores = numpy.zeros([r, c], dtype=int) + 10
    mines[0,0] = 0
    return mines, scores

def update_scores(mines, scores):
    for i in range(mines.shape[0]):
        for j in range(mines.shape[1]):
            if mines[i,j] == 0:
                scores[i,j] = numpy.sum(get_sub_matrix(mines, i, j))

def build_output(scores):
    result = ''
    found_c = False
    for i in range(scores.shape[0]):
        result += '\n';
        for j in range(scores.shape[1]):
            if not found_c and scores[i,j] == 0:
                found_c = True
                result += 'C'
            elif scores[i,j] < 10:
                result += '.'
            else:
                result += '*'

    return result

if __name__ == '__main__':
    t0 = time.clock()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"

    input_file = open(filename, "r")
    output_file = open(filename.replace('in','out'), "w")
    case_count = int(input_file.readline())
    for i in range(case_count):
        result = process_case(parse_case(input_file))
        output_line = 'Case #%d: %s\n' % (i+1, result)
        print(output_line)
        output_file.writelines(output_line)

    input_file.close()
    output_file.close()

    print('Total Time: %s' % str(time.clock() - t0))