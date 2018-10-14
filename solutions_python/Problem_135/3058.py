
def solve():
    with open('A-small-attempt0.in', 'r') as input_f:
        T = int(input_f.readline())
        for case in range(0, T):
            first_choice = int(input_f.readline()) - 1
            # Read first card matrix
            first_matrix = [map(int, input_f.readline().split()) for _ in range(0, 4)]

            second_choice = int(input_f.readline()) - 1
            # Read second card matrix
            second_matrix = [map(int, input_f.readline().split()) for _ in range(0, 4)]

            first_row = first_matrix[first_choice]

            second_row = second_matrix[second_choice]

            first_set = set(first_row)
            second_set = set(second_row)

            intersection = first_set & second_set

            intersection_size = len(intersection)
            if intersection_size == 0:
                solution = 'Volunteer cheated!'
            elif intersection_size == 1:
                solution = intersection.pop()
            else:
                solution = 'Bad magician!'

            print 'Case #%s: %s' % (case + 1, solution)

if __name__ == '__main__':
    solve()


