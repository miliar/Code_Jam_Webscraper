# -*- coding: utf-8 -*-  
DATA_FILE_NAME = 'A-large.in'
# DATA_FILE_NAME = 'B-large-practice.in'
# DATA_FILE_NAME = 'test_data_b.dat'
#DATA_FILE_NAME = 'test1.in'
SHELL_PIPE_FLAG = False
# =================================================================
def data_iterator(lines_to_read=None):
    if not SHELL_PIPE_FLAG:
        with open(DATA_FILE_NAME, 'r') as f_handle:
            line_iter = f_handle.xreadlines()
            case_no = int(line_iter.next())
            for idx in range(case_no):
                if not lines_to_read:
                    line_no = int(line_iter.next())
                    yield idx + 1, [line_iter.next().strip() for _ in range(line_no)]
                else:
                    yield idx + 1, [line_iter.next().strip() for _ in range(lines_to_read)]
    else:
        import sys  # raw_input() sys.stdin.readline()
        case_no = int(sys.stdin.readline())
        for idx in range(case_no):
            if not lines_to_read:
                line_no = int(sys.stdin.readline())
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(line_no)]
            else:
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(lines_to_read)]


result_out = ''
def c1(M):
    x0 = M[0]
    count = 0
    for i in xrange(1, len(M)):
        x1 = M[i]
        if x1 > x0:
            n = 0
        else:
            n = x0 -x1
        x0 = x1
        count += n
    return count
def c2(M):
    x0 = M[0]
    count = 0
    m2 = []
    for i in xrange(1, len(M)):
        x1 = M[i]
        if x1 > x0:
            n = 0
        else:
            n = x0 -x1
            m2.append(n)
        x0 = x1
    speed = max(m2)
    for j in range(len(M)-1):
        i = M[j]
        if i <= speed:
            count += i
        else:
            count += speed
    return count

def solve(data_in):
    case_id, case_data = data_in
    M = map(int, case_data[1].split())

    case_out = c1(M), c2(M)
    return case_id, case_out


for idx, case_data in data_iterator(lines_to_read=2):
    (_, case_out) = solve((idx, case_data))
    # print case_data
    # print '========================'
    result_out += 'Case #%d: %d %d \n' % (idx, case_out[0], case_out[1])
print result_out

if not SHELL_PIPE_FLAG:
    import os

    if not os.path.exists('Out'):
        os.makedirs('Out')

    with open('./Out/' + DATA_FILE_NAME + '.out', 'wb') as f:
        f.write(result_out)

