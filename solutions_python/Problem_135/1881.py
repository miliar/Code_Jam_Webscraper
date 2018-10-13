__author__ = 'janux'


def read_scenario():
    answer = int(raw_input())
    grid = []
    for i in range(4):
        grid.append(raw_input().split())
    return answer, grid

T = int(raw_input())

for test in range(0, T):
    first_answer, first_grid = read_scenario()
    second_answer, second_grid = read_scenario()
    mark = {}
    for i in range(4):
        mark[i] = sum([second_grid[i].count(x) for x in first_grid[first_answer - 1]])
    match = mark[second_answer - 1]
    if match < 1:
        print 'Case #%d: %s' % ((test + 1), 'Volunteer cheated!')
    elif match == 1:
        result = (set(first_grid[first_answer - 1]) & set(second_grid[second_answer - 1])).pop()
        print 'Case #%d: %s' % ((test + 1), str(result))
    else:
        print 'Case #%d: %s' % ((test + 1), 'Bad magician!')


