import sys
sys.path.append('/Users/jakemagner/Desktop/google_code_jam/year_2017/')

from random import randint


from util.io import get_only_file_in_downloads


# Problem 2
def is_tidy(x):
    str_x = str(x)
    for i in xrange(len(str_x) - 1):
        if int(str_x[i]) > int(str_x[i + 1]):
            return False
    return True


def linear_last_tidy_int(N):
    last_tidy = 0
    for i in xrange(N + 1):
        if is_tidy(i):
            last_tidy = i
    return last_tidy


def log_last_tidy(N):
    if N < 10:
        return N
    digits_rev = [int(d) for d in str(N)][::-1]
    last_dig_ind = None
    for i in xrange(len(digits_rev) - 1):
        if digits_rev[i] >= digits_rev[i + 1]:
            continue
        last_dig_ind = i + 1
        digits_rev[last_dig_ind] -= 1
    if last_dig_ind is None:
        return N
    for i in xrange(last_dig_ind):
        digits_rev[i] = 9
    return int(''.join([str(d) for d in digits_rev[::-1]]))


def compare_funcs(f1, f2, inputs):
    for input_ in inputs:
        if f1(input_) != f2(input_):
            print 'Failed for %d' % input_


def generate_output(intput_lines):
    cases = None
    for i, line in enumerate(intput_lines):
        if i == 0:
            cases = int(line.strip())
            continue
        if i > cases:
            break
        print 'Case #%d: %d' % (i, log_last_tidy(int(line.strip())))


def generate_input(T, N, target_file):
    target_file.write('%d\n' % T)
    for case in xrange(T):
        target_file.write('%d\n' % randint(1, N))
    target_file.close()


if __name__ == '__main__':
    path = None
    if len(sys.argv) == 2:
        path = sys.argv[1]
    if path is None:
        input_file = get_only_file_in_downloads()
    else:
        input_file = open(path)
    generate_output(input_file)
