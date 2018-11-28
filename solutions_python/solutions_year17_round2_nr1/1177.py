def main():
    solutions = []
    with open('A-large.in', 'r') as f:
        rows = f.readlines()
        T = int(rows[0])
        row_counter = 1
        for i in xrange(T):
            row = rows[row_counter]
            row_splitted = row.split(' ')
            D = int(row_splitted[0])
            N = int(row_splitted[1])
            max_remaining_hours = 0
            for j in xrange(1, N+1):
                second_row_counter = row_counter + j
                second_row = rows[second_row_counter]
                second_row_splitted = second_row.split(' ')
                K = int(second_row_splitted[0])
                S = int(second_row_splitted[1])
                remaining_hours = round((D-K)/float(S), 6)
                if remaining_hours > max_remaining_hours:
                    max_remaining_hours = remaining_hours
            max_allowed_speed = round(D/float(max_remaining_hours), 6)
            solutions.append(max_allowed_speed)
            row_counter += N + 1

            with open('A-large.out', 'w') as f:
                line_number = 1
                for line in solutions:
                    f.write("Case #{0}: {1}\n".format(str(line_number), line))
                    line_number += 1

main()
