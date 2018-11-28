
def flip(initial_state: str, flipper_size: int):
    initial_state = initial_state.strip('+')
    pancakes = [c == '+' for c in initial_state]
    moves = 0
    start = 0
    while True:
        try:
            start = pancakes.index(False, start)
        except ValueError:
            break
        moves += 1
        end = start + flipper_size
        if end > len(pancakes):
            return 'IMPOSSIBLE'
        for index in range(start, end):
            pancakes[index] = not pancakes[index]
    return moves


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
                    initial_state, flipper_size_raw = line.split(' ', 1)
                    flipper_size = int(flipper_size_raw)
                    result = 'Case #{}: {}\n'.format(case, flip(initial_state, flipper_size))
                    print(result)
                    outp.write(result)

if __name__ == '__main__':
    process('A-large.in')