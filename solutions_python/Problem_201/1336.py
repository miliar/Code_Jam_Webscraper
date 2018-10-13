import sys


def lp2(num):
    r = 1
    while r <= num:
        r *= 2
    return r


with open(sys.argv[1]) as f:
    num_test_cases = f.readline()
    answers = []
    for line in f:
        case = line.split()
        n = int(case[0])
        k = int(case[1])
        min = (n - k) / lp2(k)
        max = round((n - k * 1.0) / lp2(k))
        answers.append([int(max), int(min)])

with open('response.txt', 'w') as f:
    for i, answer in enumerate(answers):
        f.write('Case #%s: %s\n' % (i + 1, ' '.join([str(d) for d in answer])))
