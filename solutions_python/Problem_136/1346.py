from common import parse_input, log_output


@parse_input(file_name='B-large.in')
@log_output(file_name='B-large.out')
def main(f=None, t=None):
    for tc in range(t):
        C, F, X = map(lambda ip: float(ip), f.readline().rstrip().split(' '))
        base = X / 2
        increment = 0
        incurred = 0
        while 1:
            cost_of_farm = C / (2 + increment)
            increment += F
            time_taken = X / (2 + increment) + cost_of_farm + incurred
            if time_taken < base:
                base = time_taken
                incurred += cost_of_farm
            else:
                break
        print 'Case #%d: %.7f' % (tc + 1, base)

if __name__ == '__main__':
    main()
