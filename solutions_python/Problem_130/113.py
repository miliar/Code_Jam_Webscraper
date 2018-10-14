import sys
from math import log, floor

DEBUG = True

def get_max_initial_losses(team_n):
    return int(log(team_n+1, 2))

def get_max_initial_wins(team_n, n):
    lesser_teams = 2**n - team_n
    return int(log(lesser_teams, 2))

def highest_guaranteed_position(n, team_n):
    ret = 0
    for i in range(get_max_initial_losses(team_n)):
        ret += 2**(n-(i+1))
    return ret

def highest_possible_position(n, team_n):
    ret = 2**(n - get_max_initial_wins(team_n, n)) - 1
    return ret

def bin_search(upper, lower, n, p, f):
    # lower always possible
    # will round down
    mid = int((upper + lower) / 2)
    if mid == lower:
        return f(n, upper) <= (p-1) and upper or lower
    if f(n, mid) <= (p-1):
        return bin_search(upper, mid, n, p, f)
    else:
        return bin_search(mid, lower, n, p, f)


def solver(n, p):
    # use a binary search
    guaranteed = bin_search(2**n - 1, 0, n, p, highest_guaranteed_position)
    possible = bin_search(2**n - 1, 0, n, p, highest_possible_position)
    return str(guaranteed) + ' ' + str(possible)


def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        n, p = ssi(rl())
        answer = solver(n, p)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
