def make_int_pancakes(str_pancakes):
    return [0 if char == '-' else 1 for char in str_pancakes]

def flip_one(pancakes, idx):
    pancakes[idx] = 1 - pancakes[idx]

def flip_k(pancakes, start_idx, k):
    if len(pancakes) - start_idx < k:
        raise ValueError('Impossible')
    else:
        for k in range(k):
            flip_one(pancakes, start_idx + k)

def solve(pancakes, k):
    flips = 0
    try:
        for idx, pancake in enumerate(pancakes):
            if pancake == 0:
                flip_k(pancakes, idx, k)
                flips += 1
        return str(flips)
    except ValueError:
        return 'IMPOSSIBLE'

def main():
    case_count = int(input())
    for case_no in range(1, case_count+1):
        _pancakes, _k = input().split()
        k = int(_k)
        pancakes = make_int_pancakes(_pancakes)
        solution = solve(pancakes, k)
        print('Case #{0}: {1}'.format(case_no, solution))

if __name__ == '__main__':
    main()
