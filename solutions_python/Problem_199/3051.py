def main():
    number_of_tests = int(input())
    for case_number in range(1, number_of_tests + 1):
        case_data = input()
        case_result = solve(case_data)
        print(f'Case #{case_number}: {case_result}')

def solve(case_data):
    pancakes = case_data.split(' ')[0]
    flip_size = int(case_data.split(' ')[1])

    flip_count = 0

    for i in range(0, len(pancakes) - flip_size + 1):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, flip_size, i)
            flip_count += 1

    if '-' in pancakes:
        return 'IMPOSSIBLE'

    return str(flip_count)


def flip(pancakes, size, start):
    starting_pancakes = pancakes[0:start]
    flipped_pancakes = pancakes[start:start + size].replace('-', '|').replace('+', '-').replace('|', '+') 
    trailing_pancakes = pancakes[start + size:]
    return starting_pancakes + flipped_pancakes + trailing_pancakes

if __name__ == '__main__':
    main()
