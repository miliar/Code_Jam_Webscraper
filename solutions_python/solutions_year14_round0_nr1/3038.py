fin = open('in', 'r')
fout = open('out', 'w')

input_size = 4

num_of_cases = fin.readline()
print(num_of_cases)

def get_guess_line(guess1):
    for t in range(input_size):
        if t + 1 == guess1:
            guess1_line = fin.readline().split()
        else:
            fin.readline()
    return guess1_line


for i in range(int(num_of_cases)):
    guess1 = int(fin.readline())
    guess1_line = get_guess_line(guess1)
    guess2 = int(fin.readline())
    guess2_line = get_guess_line(guess2)
    intersect_line = set(guess1_line) & set(guess2_line)

    result = 'Case #' + str(i + 1) + ': '
    if len(intersect_line) == 0:
        fout.write(result + 'Volunteer cheated!\n')
    elif len(intersect_line) == 1:
        fout.write(result + next(iter(intersect_line)) + '\n')
    else:
        fout.write(result + 'Bad magician!\n')

fin.close()
fout.close()
