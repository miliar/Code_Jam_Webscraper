import sys
import collections


TestCase = collections.namedtuple('TestCase', ['id', 'answers', 'squares'])


def read_line():
    return sys.stdin.readline().strip()



def read_inputs():
    n_tests = int(read_line())
    tests = []
    for case_id in range(1, n_tests + 1):
        answers = []
        squares = []
        for _ in range(2):
            answers.append(int(read_line()))
            sq = [[int(x) for x in read_line().split()]
                  for _ in range(4)]
            squares.append(sq)
        tests.append(TestCase(case_id, answers, squares))

    return tests

def solve(tid, answers, squares):
    cards = set(squares[0][answers[0] - 1]) & set(squares[1][answers[1] - 1])
    ans = None
    if len(cards) == 0:
        ans = 'Volunteer cheated!'
    elif len(cards) == 1:
        ans = str(list(cards)[0])
    else:
        ans = 'Bad magician!'
    return 'Case #{}: {}'.format(tid, ans)


tcs = read_inputs()
for tc in tcs:
    print(solve(*tc))
