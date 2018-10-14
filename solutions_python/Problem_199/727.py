import re

def main():
    file = open('A-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))

    for case_idx in range(0, case_count):
        flip_count = 0  # First switch we don't count

        m = re.search('([+-]+)\s(\d+)', next(lines))
        pancakes = list(m.group(1))
        k = int(m.group(2))

        stop = len(pancakes) - k + 1
        for p_idx in range(stop):
            if pancakes[p_idx] == '-':
                flip_count += 1
                for k_idx in range(p_idx, p_idx + k):
                    pancakes[k_idx] = '+' if pancakes[k_idx] == '-' else '-'

        flip_result = 'IMPOSSIBLE'
        if '-' not in pancakes[-k:]:
            flip_result = str(flip_count)
        print(f'Case #{case_idx  + 1}: {flip_result}')


if __name__ == '__main__':
    main()