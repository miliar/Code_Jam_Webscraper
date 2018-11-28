def parse_line():
    plus_minus, flipper_size = input().strip().split()
    pancakes = [(False if ch == '-' else True) for ch in plus_minus]
    flipper_size = int(flipper_size)
    return pancakes, flipper_size

def flip(i, pancakes, flipper_size):
    for j in range(i, i + flipper_size):
        pancakes[j] = not pancakes[j]


def all_happy(pancakes):
    for pancake in pancakes:
        if not pancake:
            return False

    return True


def main():
    T = int(input())

    for case_num in range(1, T+1):
        pancakes, flipper_size = parse_line()
        num_flips = 0
        for i in range(len(pancakes) - flipper_size + 1):
            is_happy = pancakes[i]
            if not is_happy:
                flip(i, pancakes, flipper_size)
                num_flips += 1

        ans = num_flips if all_happy(pancakes) else 'IMPOSSIBLE'
        print('Case #', case_num, ': ', ans, sep='')



if __name__ == '__main__':
    main()