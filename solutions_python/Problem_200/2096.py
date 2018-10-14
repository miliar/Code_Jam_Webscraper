#!env python

def main(input_file='input.txt', output_file='output.txt'):
    fd = open(input_file)
    cases = int(fd.readline())
    output = open(output_file, 'w')

    for i in range(cases):
        N = int(fd.readline())

        response = find_tidy(N)
        line = 'Case #%d: %s' % (i + 1, response)

        print line
        output.writelines([line, '\n'])

def find_tidy(N):
    tidy_decrease = 1
    while not is_tidy(str(N)):
        N = get_next_N(N)
    return N

def is_tidy(str_N):
    prev = str_N[0]
    for n in str_N[1:]:
        if prev > n:
            return False
        prev = n

    return True

def get_next_N(N):
    str_N = str(N)

    prev = str_N[0]
    for i, n in enumerate(str_N[1:]):
        if n < prev:
            rest = int(str_N[i + 1:]) or 1
            return N - rest
        prev = n

    # for consistency
    return N - 1

if __name__ == '__main__':
    main(input_file='B-large.in')
