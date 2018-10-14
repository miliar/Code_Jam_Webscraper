import sys

DEBUG = True

def check_palindrome(n):
    str_n = str(n)
    len_n = len(str_n)
    for i in xrange(len_n / 2):
        if str_n[i] != str_n[(len_n - 1) - i]:
            return False
    return True

def fairs_and_squares(max):
    fairs_and_squares = []
    sqrt_max = max**(0.5)
    i = 1
    while i < sqrt_max:
        if check_palindrome(i):
            sqr_i = i**2
            if check_palindrome(sqr_i):
                fairs_and_squares.append(sqr_i)
        i += 1
    return fairs_and_squares


def solver(a, b, candidates):
    lower_idx = 0
    while lower_idx < len(candidates) and candidates[lower_idx] < a:
        lower_idx += 1
    upper_idx = lower_idx
    while upper_idx < len(candidates) and candidates[upper_idx] <= b:
        upper_idx += 1

    return upper_idx - lower_idx

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
    candidates = fairs_and_squares(10**14)
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        a, b = ssi(rl())
        answer = solver(a, b, candidates)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
