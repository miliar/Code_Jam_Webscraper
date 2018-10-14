import sys

def read_board():
    for i in range(4):
        yield [int(n) for n in sys.stdin.readline().split()]

def get_response():
    answer = int(sys.stdin.readline())
    return list(read_board())[answer - 1]

def play():
    first = set(get_response())
    second = set(get_response())
    common = list(first.intersection(second))

    if not common:
        return 'Volunteer cheated!'
    elif len(common) > 1:
        return 'Bad magician!'
    else:
        return common[0]

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline())

    for i in range(num_cases):
        result = play()
        print('Case #{}: {}'.format(i + 1, result))
