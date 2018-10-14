from math import ceil
import sys

def max_score_surprise(t):
    ms = int(ceil(t / 3.))
    if t % 3 == 0:
        ms += 1
    if t % 3 == 2:
        ms += 1
    return min(t, ms)

def find_num_p(N, S, p, ts):
    valid_ts = []
    unsure_ts = []

    for t in ts:
        if int(ceil(t/3.)) >= p:
            valid_ts.append(t)
        else:
            unsure_ts.append(t)

    valid_s_ts = []
    unsure_s_ts = []

    for t in unsure_ts:
        if len(valid_s_ts) >= S:
            break
        if max_score_surprise(t) >= p:
            valid_s_ts.append(t)
        else:
            unsure_s_ts.append(t)
    
    num_s = min(len(valid_s_ts), S)

    return len(valid_ts) + num_s

infile_name = sys.argv[1]

with open(infile_name, 'r') as infile:
    with open(infile_name + '.out', 'w') as outfile:
        n_inputs = int(infile.readline().strip())
        for i, line in enumerate(infile):
            i += 1
            if i > n_inputs:
                break
            params = line.split()
            N = int(params[0])
            S = int(params[1])
            p = int(params[2])
            ts = [int(t) for t in params[3:]]
            num_p = find_num_p(N, S, p, ts)

            outline = "Case #%d: %d\n" % (i, num_p)
            outfile.write(outline)

