import os
import sys

debug_mode = False
if debug_mode:
    debug_fd = sys.stdout
else:
    debug_fd = open(os.devnull, "w")


def read_input():
    N, K = map(int, raw_input().split())
    return N, K

def calculate(input_args):
    N, K = input_args

    spaces = {}
    spaces[N] = 1

    max_space = N
    while K > 0:
        l = (max_space - 1) / 2
        r = max_space - 1 - l

        cnt = spaces[max_space]
        if K >= cnt:
            this_patch = cnt
        else:
            this_patch = K
        K -= this_patch

        spaces[max_space] -= this_patch
        spaces[l] = spaces.get(l, 0) + this_patch
        spaces[r] = spaces.get(r, 0) + this_patch

        if spaces[max_space] == 0:
            del spaces[max_space]
            max_space = max(spaces.keys())

    return sorted((l, r), reverse=True)

def to_formated_string(result_tokens):
    ans_str = " ".join(map(str, result_tokens))
    return ans_str

if __name__ == '__main__':
    T = int(raw_input())
    case = 1
    while case <= T:
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer
        case += 1

