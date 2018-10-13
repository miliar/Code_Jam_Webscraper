import random, sys

def readints(f):
    return set(int(s) for s in f.readline().split())

def magic_solver(guess_one, deck_one, guess_two, deck_two):
    first_row = deck_one[guess_one - 1]
    second_row = deck_two[guess_two - 1]

    answer = first_row.intersection(second_row)

    if len(answer) == 0:
        return 'Volunteer Cheated!'
    elif len(answer) > 1:
        return 'Bad Magician!'
    else:
        return answer.pop()

def magic_reader(goog_file):
    answers = []

    with open(goog_file, 'r') as f:
        data_sets = int(f.readline())
        for tricks in xrange(0, data_sets):
            deck_one = []
            deck_two = []
            guess_one = int(f.readline())
            for deck_row in xrange(0, 4):
                deck_one.append(readints(f))
            guess_two = int(f.readline())
            for deck_row in xrange(0, 4):
                deck_two.append(readints(f))

            answers.append(magic_solver(guess_one, deck_one, guess_two, deck_two))

    return answers


answers = magic_reader(sys.argv[1])
with open('A.out', 'w') as out_file:
    for i, answer in enumerate(answers):
        out_file.write('Case #' + str(i + 1) + ': ' + str(answer) + '\n')
