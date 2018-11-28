import sys, os, re, collections

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))

def create (trial, i, result_so_far):
    if i == len(trial):
        return int(''.join(map(str,result_so_far)))
    cur = int(trial[i])
    prev = result_so_far[-1]
    if cur < prev:
        return None
    elif cur > prev:
        r = create(trial, i+1, result_so_far + [cur])
        if r is None:
            n_trial = trial[:i] + [cur - 1] + [9]*(len(trial) - i - 1)
            assert len(n_trial) == len(trial)
            r = create(n_trial, i+1, result_so_far + [cur-1])
            assert r is not None
        return r
    else:
        return create(trial, i+1, result_so_far + [cur])

for case_num in range(int(input())):
    bound = [int(a) for a in input()]
    result = create(bound, 0, [0])
    print_result(case_num, result)
