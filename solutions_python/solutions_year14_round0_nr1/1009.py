input_file = "A-small-attempt0.in"

with open("magic_trick.out", 'w') as output:
    with open(input_file, 'r') as f:
        n_cases = int(f.readline())

        numbers = list(range(1, 17))

        for i in range(n_cases):
            first_answer = int(f.readline())
            first_table = []
            for j in range(4):
                row = [int(i) for i in f.readline().split(' ')]
                first_table.append(row)

            second_answer = int(f.readline())
            second_table = []
            for j in range(4):
                row = [int(i) for i in f.readline().split(' ')]
                second_table.append(row)

            valid_numbers, invalid_numbers = [], []
            first_valid_row = first_table[first_answer - 1]
            second_valid_row = second_table[second_answer - 1]

            valid_numbers = set(first_valid_row) & set(second_valid_row)

            if len(valid_numbers) == 1:
                answer = valid_numbers.pop()
            elif len(valid_numbers) > 1:
                answer = "Bad magician!"
            else:
                answer = "Volunteer cheated!"

            output.write("Case #{case_number}: {answer}\n".format(case_number=i + 1, answer=answer))