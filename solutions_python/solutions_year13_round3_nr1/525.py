#!/usr/bin/env python

def get_num_strings(name, n):
    substrings = []
    for i in range(len(name)):
        for j in range(i + 1, len(name) + 1):
            substrings.append(name[i:j])

    num_strings = 0
    for ss in substrings:
        vow_idx = [-1]
        is_n_value = False
        for i in range(len(ss)):
            if ss[i] in ['a', 'e', 'i', 'o', 'u']:
                vow_idx.append(i)
            last_idx = len(vow_idx) - 1
            if last_idx - 1 >= 0 and vow_idx[last_idx] - vow_idx[last_idx - 1] > n:
                is_n_value = True
                num_strings += 1
                break
        if not is_n_value and len(ss) - vow_idx[len(vow_idx) - 1] > n:
            num_strings += 1

    return num_strings

if __name__ == '__main__':
    tc = int(raw_input())
    for t in range(1, tc + 1):
        inp = raw_input().split()
        name, n = inp[0], int(inp[1]) 
        print 'Case #{t}: {num_strings}'.format(t=t, num_strings=get_num_strings(name, n))
