import sys

with open(sys.argv[1]) as f:
    num_test_cases = f.readline()
    answers = []
    for line in f:
        newline = line.strip()
        num = [int(d) for d in newline]
        for i in xrange(len(num) - 1, 0, -1):
            if num[i] < num[i - 1]:
                num[i:] = [9] * len(num[i:])
                num[i - 1] -= 1
        answers.append(''.join([str(d) for d in num]).strip('0'))

with open('response.txt', 'w') as f:
    for i, answer in enumerate(answers):
        f.write('Case #%s: %s\n' % (i + 1, str(answer)))
