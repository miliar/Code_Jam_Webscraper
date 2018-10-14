import os.path, glob
PROBLEM = os.path.basename(__file__)[0].upper()
DL_DIR = os.path.join(os.environ['USERPROFILE'], 'Downloads', PROBLEM)
if os.path.exists(DL_DIR + '-large.in'):
    INP_PATH = DL_DIR + '-large.in'
    OUT_PATH = DL_DIR + '-large.ot'
else:
    inputs = glob.glob(DL_DIR + '-small-attempt[0-9].in')
    maxnum = -1
    for inp_fn in inputs:
        if int(inp_fn[-4]) > maxnum: maxnum = int(inp_fn[-4])
    if maxnum > -1:
        INP_PATH = DL_DIR + '-small-attempt' + str(maxnum) + '.in'
        OUT_PATH = DL_DIR + '-small-attempt' + str(maxnum) + '.ot'
    else:
        INP_PATH = os.path.join('..', 'data', PROBLEM + '.in')
        OUT_PATH = os.path.join('..', 'data', PROBLEM + '.ot')

in_file = open(INP_PATH)
out_file = open(OUT_PATH, 'w')

def pp(s):
    out_file.write(s + '\n')
    print s


def strof(f):
    if float(int(f)) != f:
        return str(f)
    return str(int(f))

NUM_CASES = int(in_file.readline().strip())
for case in range(1, NUM_CASES + 1):
    soln = ''
    dat = in_file.readline().strip().split()
    n = int(dat[0])
    w = int(dat[1])
    l = int(dat[2])
    
    radii = map(int, in_file.readline().strip().split())
    student_mapping = list(enumerate(radii))
    student_mapping.sort(key=lambda x:x[1], reverse=True)
    positions = [None] * n
    positions[student_mapping[0][0]] = (0, 0)
    last_x = 0
    last_y = 0
    row_started = 0
    next_row = student_mapping[0][1]
    last_rad = student_mapping[0][1]
    skipped = False
    for student in student_mapping:
        if not skipped:
            skipped = True
            continue
        rad = student[1]
        if last_x + last_rad + rad > w:
            positions[student[0]] = (0, next_row + rad)
            next_row = next_row + 2 * rad
            last_x, last_y = positions[student[0]]
            last_rad = rad
        else:
            positions[student[0]] = (last_x + rad + last_rad, last_y)
            last_x = last_x + rad + last_rad
            last_rad = rad
        if last_y > l:
            print 'UH OH'
#        print last_x, last_y, w, l
    op = []
    for p in positions:
        op.append(' '.join(map(strof, p)))
            
    pp('Case #' + str(case) + ': ' + ' '.join(op))
    
    
out_file.close()
in_file.close()
