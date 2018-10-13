__author__ = 'panmari'


filename = 'B-small-attempt0.in'

answers = []
with open(filename) as file:
    nr_problems = int(file.readline())
    while True:
        nextLine = file.readline().strip()
        if nextLine == '':
            break
        M1, M2, K = map(lambda x: int(x), nextLine.split(' '))
        win_case = 0
        for m1 in range(M1):
            for m2 in range(M2):
                if m1 & m2 < K:
                    win_case += 1

        answers.append('{}'.format(win_case))


with open(filename + '.out', 'w') as f:
    for n, answer in enumerate(answers):
        f.write("Case #{}: {}\n".format(n + 1, answer))