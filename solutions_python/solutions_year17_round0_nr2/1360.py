import sys


def is_ok(data:str)->bool:
    prev = 0
    for c in map(int, list(data)):
        if c < prev:
            return False
        prev = c
    return True


def do(data:str) -> str:
    result = []
    is_reduced = False
    for i, current in enumerate(data):
        c = int(current)
        if is_reduced:
            c = 9
        elif i < len(data) - 1:
            if c > int(data[i+1]):
                c -= 1
                is_reduced = True
        result.append(str(c))
    result = ''.join(result).lstrip('0')
    return result


def solve(data:str) -> str:
    while not is_ok(data):
        data = do(data)
    return data

def parse(prob:str):
    return {
        'data': prob.strip('\n'),
    }

def main():
    filename = sys.argv[1]
    with open(filename) as fp:
        num_prob, *data = fp.readlines()
        for idx, prob in enumerate(map(parse, data), start=1):
            result = solve(**prob)
            print(f'Case #{idx}: {result}')

if __name__ == '__main__':
    main()
