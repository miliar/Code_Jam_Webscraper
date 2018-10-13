import sys


def output(answers):
    case_num = 1
    for y,z in answers:
        print 'Case #%d: %s %s' % (case_num, y, z)
        case_num += 1


def get_input():
    num_cases = int(sys.stdin.readline())

    for case in range(num_cases):
        num_samples = int(sys.stdin.readline())
        samples = [int(mi) for mi in sys.stdin.readline().split()]

        yield (num_samples, samples)


def solve(cases):
    for num_samples,samples in cases:
        decreases = [max(0, x-y) for x,y in zip(samples, samples[1:])]

        first = sum(decreases)
        
        max_decrease = max(decreases)
        
        second = sum(min(x, max_decrease) for x in samples[:-1])
        
        yield first, second


def main():
    cases = get_input()
    answers = solve(cases)
    output(answers)


if __name__ == '__main__':
    main()

