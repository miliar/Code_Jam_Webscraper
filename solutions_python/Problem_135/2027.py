def solve():
    first_row_number = input()
    lines = [raw_input() for _ in range(4)]
    first_row = set(lines[first_row_number - 1].split())
    second_row_number = input()
    lines = [raw_input() for _ in range(4)]
    second_row = set(lines[second_row_number - 1].split())
    possible_answers = first_row & second_row
    if len(possible_answers) > 1:
        return "Bad magician!"
    elif len(possible_answers) == 1:
        return possible_answers.pop()
    else:
        return "Volunteer cheated!"


cases = input()
output = []
for case in range(cases):
    output.append("Case #{}: {}".format(case + 1, solve()))
with open('output.txt', 'w') as file:
    file.write('\n'.join(output))