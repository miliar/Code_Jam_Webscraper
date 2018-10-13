#codeing=utf8

import sys


def main(infile, outfile):
    lines = open(infile, 'r').readlines()
    case_num = int(lines[0].strip())
    for i in range(case_num):
        case = lines[3*i + 1:3*i + 4]
        res = get_result(case, i)
        open(outfile, 'a').write('%s\n' % res)


def get_result(case, index):
    index += 1
    N = int(case[0].strip())
    naomi = convert(case[1].strip())
    ken = convert(case[2].strip())
    score = get_score(naomi, ken, N)
    deceit_score = get_deceit_score(naomi, ken, N)
    return 'Case #%d: %d %d' % (index, deceit_score, score)


def convert(data):
    float_list = []
    s = data.split()
    for i in s:
        float_list.append(float(i))
    return sorted(float_list, reverse=True)


def get_score(naomi, ken, N):
    score = 0
    if N == 1:
        if naomi[0] > ken[0]:
            return 1
        else:
            return 0
    n_begin = 0
    n_end = N - 1
    k_begin = 0
    k_end = N - 1
    while n_begin <= n_end:
        if naomi[n_begin] > ken[k_begin]:
            n_begin += 1
            k_end -= 1
            score += 1
        else:
            n_begin += 1
            k_begin += 1
    return score


def get_deceit_score(naomi, ken, N):
    score = 0
    if N == 1:
        if naomi[0] > ken[0]:
            return 1
        else:
            return 0
    n_begin = 0
    n_end = N - 1
    k_begin = 0
    k_end = N - 1
    naomi = sorted(naomi)
    ken = sorted(ken)
    while n_begin <= n_end:
        if naomi[n_begin] < ken[k_begin]:
            n_begin += 1
            k_end -= 1
        else:
            n_begin += 1
            k_begin += 1
            score += 1
    return score


main(sys.argv[1], sys.argv[2])