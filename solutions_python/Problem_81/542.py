import os
from copy import deepcopy

INFILE = r'C:\Users\noam\workspace\CodeJam\input.txt'

def parse_lines(line):
    return list(x for x in line.strip().split() if x)

def calc_wp(stats, idx):
    won = float(get_won(stats, idx))
    played = float(get_played(stats, idx))
    return  won / played

def calc_owp(stats, idx):
    stat_copy = deepcopy(stats)
    opponents = [i for i in xrange(len(stats)) if (stats[idx][i] != '.')]
    
    acc = 0.0
    for op_idx in opponents:
        stat_copy[op_idx].pop(idx)
        acc += float(calc_wp(stat_copy, op_idx))
    return acc / float(get_played(stats, idx))

def calc_oowp(stats, idx):
    acc = 0.0
    opponents = [i for i in xrange(len(stats)) if (stats[idx][i] != '.')]
    for op_idx in opponents:
        acc += calc_owp(stats, op_idx)
    return acc / float(get_played(stats, idx))

def get_played(stats, idx):
    l = stats[idx]
    return l.count('1') + l.count('0')

def get_won(stats, idx):
    l = stats[idx]
    ret = l.count('1')
    return ret

def get_lost(stats, idx):
    l = stats[idx]
    return l.count('0')
    
def solve(stats):
    ret = []
    for idx in xrange(len(stats)):
        wp = calc_wp(stats, idx)
        owp = calc_owp(stats, idx)
        oowp = calc_oowp(stats, idx)
        ret.append(0.25*wp + 0.50*owp + 0.25*oowp)
    return ret

def res_to_str(res):
    return '\n'.join(str(x) for x in res)

def main():
    infile = file(INFILE)
    outfile = file(INFILE + '.result.txt', 'wt')
    test_case = 0
    infile.readline()
    while infile.tell() != os.SEEK_END:
        test_case += 1
        line1 = infile.readline()
        if not line1.strip():
            return
        teams_num = int(line1)
        stats = []
        for _ in xrange(teams_num):
            line = infile.readline().strip()
            stats.append(list(line))
        res = solve(stats)
        str_res = res_to_str(res)
        res_line = 'Case #%d:\n%s\n' % (test_case, str_res)
        print res_line,
        outfile.write(res_line)
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()

