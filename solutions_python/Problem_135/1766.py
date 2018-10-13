f_input = open('A-small-attempt3.in')
lines = f_input.read().split('\n')
f_input.close()
case = 0
first_guess = second_guess = ''
first_set = second_set = []

f_output = open('result.txt', 'w')

lines.pop(0)
for line_index in range(0, len(lines), 10):
    case = case + 1
    first_set = []
    first_set.append(lines[line_index + 1].split(' '))
    first_set.append(lines[line_index + 2].split(' '))
    first_set.append(lines[line_index + 3].split(' '))
    first_set.append(lines[line_index + 4].split(' '))
    first_guess = set(first_set[int(lines[line_index]) - 1])

    second_set = []
    second_set.append(lines[line_index + 6].split(' '))
    second_set.append(lines[line_index + 7].split(' '))
    second_set.append(lines[line_index + 8].split(' '))
    second_set.append(lines[line_index + 9].split(' '))
    second_guess = set(second_set[int(lines[line_index + 5]) - 1])

    guess = first_guess & second_guess
    result = 'Case #{}: {}\n'
    resutl_text = ''
    if len(guess) == 1:
        resutl_text = result.format(case, guess.pop())
    elif len(guess) > 1:
        resutl_text = result.format(case, 'Bad magician!')
    else:
        resutl_text = result.format(case, 'Volunteer cheated!')

    f_output.write(resutl_text)

f_output.close()

