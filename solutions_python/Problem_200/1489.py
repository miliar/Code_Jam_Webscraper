
def solution(last_number_str):
    last_tidy_pieces = []
    previous_number = None
    for ch in reversed(last_number_str):
        num = int(ch)
        if previous_number is None:
            previous_number = num
            last_tidy_pieces.append(num)
        else:
            if num > last_tidy_pieces[-1]:
                last_tidy_pieces = [9] * len(last_tidy_pieces)
                new_num = num - 1
            else:
                new_num = num
            last_tidy_pieces.append(new_num)
            previous_number = new_num
    return ''.join(str(num) for num in reversed(last_tidy_pieces)).lstrip('0')


def process(filepath):
    with open(filepath.replace('.in', '.out'), 'w') as outp:
        with open(filepath) as filep:
            inputs = None
            case = 0
            for line in filep:
                line = line.strip()
                if inputs is None:
                    inputs = int(line)
                else:
                    case += 1
                    result = 'Case #{}: {}\n'.format(case, solution(line))
                    print(result, end='')
                    outp.write(result)

if __name__ == '__main__':
    process('B-large.in')