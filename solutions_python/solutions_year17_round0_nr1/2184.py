CORRECT_SIDE = '+'

def flip_pancakes(pancakes, start_idx, k):
    while k > 0:
        k -= 1
        try:
            pancakes[start_idx + k] = not pancakes[start_idx + k]
        except IndexError:
            return None

    return pancakes

def get_num_flips(pancakes, k):
    pancakes = [x == CORRECT_SIDE for x in pancakes]

    num_flips = 0
    idx = 0
    while idx < len(pancakes):
        if not pancakes[idx]:
            pancakes = flip_pancakes(pancakes, idx, k)
            if pancakes is None:
                return 'IMPOSSIBLE'
            num_flips += 1
        idx += 1
    return num_flips

def main():
    filename = 'A-large.in'

    with open(filename, 'r') as input_file:
        num_tests = int(input_file.readline().strip())
        test_number = 1

        while test_number <= num_tests:
            pancakes, flipper_width = input_file.readline().split()
            ans = get_num_flips(pancakes, int(flipper_width))
            print 'Case #{}: {}'.format(test_number, ans)

            test_number += 1

if __name__ == '__main__':
    main()
