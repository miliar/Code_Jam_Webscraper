import sys

def solve_line(n, s, p, *scores):
    '''
     N, the number of Googlers
     S, the number of surprising triplets of scores
     result of at least p
    '''
    answer = 0
    no_surprise_range = range(max(p*3 - 2, 0), 31)
    surprise_range = range(max(p*3 - 4, 2), min(p*3 - 2, 31))
    in_no_surprise_range = 0
    in_surprise_range = 0
    for score in scores:
        if score in no_surprise_range:
            in_no_surprise_range += 1
        if score in surprise_range:
            in_surprise_range += 1
    return in_no_surprise_range + min(in_surprise_range, s)

def calc_maxs(intxt):
    lines = intxt.split('\n')
    lines_total = int(lines[0])
    outtxt = ''
    for line_num in range(1, lines_total + 1):
        outtxt += "Case #%s: %s\n" % (line_num, solve_line(*map(int, lines[line_num].split(' '))))
    return outtxt[:-1]

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r') as _ifile:
        with open(outfile, 'wb') as _ofile:
            _ofile.write(calc_maxs(_ifile.read()))
