TEST_FILE = 'A-large.in'

def main():

    f = open(TEST_FILE, 'r')
    s = open('opf-output-large.txt', 'w')
    num_test_cases = int(f.readline())

    for test_case in range(1, num_test_cases+1):
        l = f.readline().split()
        pancakes_setup = list(l[0])
        for i, pancake in enumerate(pancakes_setup):
            if pancake == '+':
                pancakes_setup[i] = 1
            else:
                pancakes_setup[i] = 0
        n = int(l[1])

        result = solve(pancakes_setup, n)
        s.write('Case #{}: {}\n'.format(test_case, result))

    f.close()
    s.close()



def solve(p, n):
    print('pancakes = ', p, 'n = ', n, ' ------------------- ')

    flips = 0
    for index in range(0, len(p) + 1 - n):



        current_pancake = p[index]

        if current_pancake == 0:  # flip the next n pancakes
            flips += 1
            for nexts in range(index, index+n):
                current_state = p[nexts]
                p[nexts] = 1 - current_state

        else:
            continue

    print(p)
    print(flips)

    if check_solved(p):
        return flips
    else:
        return 'IMPOSSIBLE'


def check_solved(pancake_string):

    return len(pancake_string) == sum(pancake_string)

if __name__ == '__main__':
    main()