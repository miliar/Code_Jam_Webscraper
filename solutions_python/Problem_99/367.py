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
        OUT_PATH = DL_DIR + '-small-' + str(maxnum) + '.ot'
    else:
        INP_PATH = os.path.join('..', 'data', PROBLEM + '.in')
        OUT_PATH = os.path.join('..', 'data', PROBLEM + '.ot')

in_file = open(INP_PATH)
out_file = open(OUT_PATH, 'w')

def pp(s):
    out_file.write(s + '\n')
    print s

from operator import mul
NUM_CASES = int(in_file.readline().strip())
for case in range(1, NUM_CASES + 1):
    so_far, total = map(int, in_file.readline().strip().split())
    odds = map(float, in_file.readline().strip().split())
    min_cost = float(total + 2)
    for bksp_count in range(so_far + 1):
        if bksp_count == so_far: success = 1.0
        else: success = reduce(mul, odds[:len(odds) - bksp_count])
        success_cost = total + bksp_count * 2 - so_far + 1
        fail_cost = 2 * total + bksp_count * 2 - so_far + 2
        cost = success_cost * success + fail_cost * (1.0 - success)
        if cost < min_cost: min_cost = cost
    soln = min_cost
    pp('Case #' + str(case) + ': %F' % soln)
    
        
out_file.close()
in_file.close()