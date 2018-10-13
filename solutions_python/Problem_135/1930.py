from functools import *

inf = open('A-small-attempt0.in')
ouf = open('output.txt', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def get_row():
    row_index = int(input()) - 1
    return set([map(int, input().split()) for i in range(4)][row_index])


def solve():
    answers = list(get_row() & get_row())
    print(['Volunteer cheated!', answers[0] if answers else None, 'Bad magician!'][min(2, len(answers))])
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()