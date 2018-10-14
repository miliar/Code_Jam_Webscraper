import sys

# Set up the input and output files
sys.stdin = open('magic.in', 'r')
sys.stdout = open('magic.out', 'w')

def main():
    # Read in T
    total_cases = int(input())
    for case_number in range(1, total_cases + 1):
        possible_numbers_1 = get_possible_numbers()
        possible_numbers_2 = get_possible_numbers()
        repeated = get_repeated(possible_numbers_1, possible_numbers_2)
        answer = ''
        if len(repeated) == 1:
            answer = repeated[0]
        elif len(repeated) == 0:
            answer = 'Volunteer cheated!'
        else:
            answer = 'Bad magician!'
        print('case #%d: %s' % (case_number, answer))

def get_possible_numbers():
    row_number = int(input()) - 1
    grid = []
    for i in range(4):
        grid.append([int(num) for num in input().split()])
    return grid[row_number]

def get_repeated(l1, l2):
    results = []
    for i in l1:
        for j in l2:
            if i == j:
                results.append(i)
    return results

if __name__ == '__main__':
    main()