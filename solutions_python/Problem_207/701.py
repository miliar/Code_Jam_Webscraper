import itertools
import sys
from collections import defaultdict



def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    groups = {'RG': 0,
            'BG': 0,
            'YG': 0}
    to_group = {'G': 'YB',
            'O': 'RY',
            'V': 'RB',
            'R': 'R',
            'B': 'B',
            'Y': 'Y'}
    i = 1
    def check_group(g):
        if set(to_group[g[0]]) & set(to_group[g[-1]]):
            return False
        for i in range(len(g) - 1):
            if set(to_group[g[i]]) & set(to_group[g[i+1]]):
                return False 
        return True

    def check_cell(prev):
        return "".join(set(to_group[prev]) ^ set('RBY'))


    while i <= test_case_count:
        N, R, O, Y, G, B, V = [int(m) for m in content[i].split(' ')]
        groups['RG'] = R + O + V
        groups['BG'] = B + G + V
        groups['YG'] = Y + G + O
        out = 'IMPOSSIBLE'
        if max(groups.values()) <= N / 2 and V <= Y and O <= B and G <= R and O + V + G <= N / 2:
            # line = ['R'] * R + ['O'] * O + ['Y'] * Y + ['G'] * G + ['B'] * B + ['V'] * V
            line = [0] * N
            index = 0
            if V:
                for v in range(V):
                    line[index] = 'V'
                    line[index+1] = 'Y'
                    index += 2
                Y -= V
            if O:
                for v in range(O):
                    line[index] = 'O'
                    line[index+1] = 'B'
                    index += 2
                B -= O
            if G:
                for v in range(G):
                    line[index] = 'G'
                    line[index+1] = 'R'
                    index += 2
                R -= G
            remainings = {'R': R, 'B': B, 'Y': Y}

            if index != 0:
                can_be = check_cell(line[index -1])
                last_can_be = check_cell(line[0])
                last_cannot_be = "".join([cc for cc in 'RBY' if cc != last_can_be])
            else:
                last_cannot_be = False
                can_be = 'RBY'
            while index < N:
                max_r = 0
                s_c = None
                if last_cannot_be:
                    maybe = set(can_be) & set(last_cannot_be)
                    for c in maybe:
                        if remainings[c] > max_r:
                            max_r = remainings[c]
                            s_c = c

                if max_r == 0:
                    for c in can_be:
                        if remainings[c] > max_r:
                            max_r = remainings[c]
                            s_c = c
                if not last_cannot_be:
                    last_cannot_be = s_c
                if max_r == 0:
                    index = N
                else:
                    line[index] = s_c
                    remainings[s_c] -= 1
                    index += 1
                can_be = "".join([c for c in 'RBY' if c != s_c])
            if 0 not in line:
                out = "".join(line)

        print("Case #%s: %s" % (i, out))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
