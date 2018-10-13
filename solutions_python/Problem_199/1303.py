import sys

with open(sys.argv[1]) as f:
    num_test_cases = f.readline()
    answers = []
    for line in f:
        case = line.split()
        state = [1 if x == '+' else 0 for x in case[0]]
        k = int(case[1])
        count = 0
        for i, pancake in enumerate(state):
            if pancake == 0:
                if len(state) < i + k:
                    count = -1
                    break
                else:
                    for j in range(k):
                        state[i + j] = (state[i + j] + 1) % 2
                    count += 1
        answers.append(count)
with open('response.txt', 'w') as f:
    for i, answer in enumerate(answers):
        f.write('Case #%s: %s\n' % (i + 1, str(answer) if answer >= 0 else 'IMPOSSIBLE'))
