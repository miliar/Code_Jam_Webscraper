import sys


def solve(input: int) -> int:
    n = list(str(input))
    length = len(n)
    # For each position except the last
    for i in range(length - 2, -1, -1):
        # Only modify if this position compared to the next is not 'tidy'
        if int(n[i]) > int(n[i + 1]):
            # Then decrement at i
            n[i] = str(int(n[i]) - 1)
            # And set all subsequent digits to 9
            for j in range(i + 1, length):
                n[j] = '9'

    return int(''.join(n))

#################################
# Parse input and solve


def run():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    results = []
    with open(input_file, 'r') as f:
        numCases = int(f.readline())
        for i in range(0, numCases):
            n = int(f.readline())

            r = solve(n)
            results.append('Case #{0}: {1}\n'.format((i + 1), r))
            print('Solved {0}/{1}'.format((i + 1), numCases))

    with open(output_file, 'w') as f:
        f.writelines(results)

    print('[Complete]')

if __name__ == '__main__':
    run()