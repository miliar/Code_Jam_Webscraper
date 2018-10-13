from time import time

startTime = time()
def expTime(pct): print int(pct * 100), "{0:.3f}".format((time() - startTime) * (1-pct) / pct)

with open('DATA.TXT') as in_file:
    # get cases
    in_arr = in_file.read().split('\n')
    num_cases = int(in_arr[0])
    case_arr = []
    row = 1
    for e in range(num_cases):
        # process txt
        case_len = 2
        case_arr.append(in_arr[row:row+case_len])
        row += case_len

def process(armin, motes):
    motes = list(sorted(motes))
    if len(motes) == 0: return 0
    if armin == 1: return len(motes)
    if armin > motes[0]: return process(armin + motes[0], motes[1:])
    # try adding a mote
    A = process(armin, motes + [armin-1])
    R = process(armin, motes[:-1])
    return min(A, R) + 1

# initialize
out = []
num = 0
for case in case_arr:
    if num % (num_cases / 10 + 1) == 1: expTime(float(num)/num_cases)
    res = 0
    # process case
    armin = int(case[0].split(' ')[0])
    motes = case[1].split(' ')
    motes = [int(e) for e in motes]
    res = process(armin, motes)
    # output
    num += 1
    out.append('Case #' + str(num) + ': ' + str(res))
    pass

# output
with open('OUT.txt', 'w') as f:
    for e in out:
        f.write(str(e) + '\n')
