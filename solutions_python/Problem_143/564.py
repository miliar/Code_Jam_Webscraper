input_file = "B-small-attempt0.in"
output_file = "new_lottery_game.out"

cases = []
with open(input_file, 'r') as f:
    n_cases = int(f.readline())

    for i in range(n_cases):
        A, B, K = (int(i) for i in f.readline().split(' '))

        cases.append((A, B, K))


def solve(case):
    a, b, k = case

    possible_a_values = list(range(a))
    possible_b_values = list(range(b))
    purchased_numbers = list(range(k))

    ways_to_win = 0
    for a_value in possible_a_values:
        for b_value in possible_b_values:
            if (a_value & b_value) in purchased_numbers:
                ways_to_win += 1

    return ways_to_win


with open(output_file, 'w') as f:
    for case_number, case in enumerate(cases):
        answer = solve(case)
        f.write('Case #{case_number}: {answer}\n'.format(case_number=case_number + 1, answer=answer))
