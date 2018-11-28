
def flip_pancake(pancake):
    return '+' if pancake == '-' else '-'


def main():
    num_cases = int(input())

    for case_num in range(1, num_cases + 1):
        pancakes, flipper_width = input().split()
        flipper_width = int(flipper_width)
        num_pancakes = len(pancakes)
        pancakes = list(pancakes)
        num_flips = 0

        for i in range(num_pancakes):
            if pancakes[i] == '-' and i + flipper_width <= num_pancakes:
                for j in range(i, i + flipper_width):
                    pancakes[j] = flip_pancake(pancakes[j])
                num_flips += 1

        if not all(pancake == '+' for pancake in pancakes):
            num_flips = 'IMPOSSIBLE'

        print('Case #{}: {}'.format(case_num, num_flips))


if __name__ == '__main__':
    main()