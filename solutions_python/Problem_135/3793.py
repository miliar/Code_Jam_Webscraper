def read_arrangement():
    arrangement = []

    for row in range(4):
        arrangement.append([int(x) for x in input().split()])

    return arrangement


cases = int(input())

for case in range(1, cases + 1):
    first_answer = int(input()) - 1
    first_arrangement = read_arrangement()

    second_answer = int(input()) - 1
    second_arrangement = read_arrangement()

    answer = set(first_arrangement[first_answer]) & set(second_arrangement[second_answer])
    answer_len = len(answer)

    if answer_len == 0:
        print('Case #{0}: Volunteer cheated!'.format(case))
    elif answer_len == 1:
        print('Case #{0}: {1:d}'.format(case, answer.pop()))
    else:
        print('Case #{0}: Bad magician!'.format(case))

