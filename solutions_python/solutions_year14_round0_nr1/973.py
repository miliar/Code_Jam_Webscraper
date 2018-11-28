
def solve(a1, grid1, a2, grid2):
    possible_answers = grid1[a1 - 1]
    possible_answers2 = grid2[a2 - 1]
    correct = set(possible_answers).intersection( set(possible_answers2))

    if len(correct) == 0:
        return 'Volunteer cheated!'
    elif len(correct) > 1:
        return 'Bad magician!'
    else:
        return str(correct.pop())


#with open('sample.in') as f:
with open('A-small-attempt0.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        answer_1 = int(f.readline())

        grid1 = {}
        for i in range(0, 4):
            grid1[i] = map(int, f.readline().split(' '))

        answer_2 = int(f.readline())

        grid2 = {}
        for i in range(0, 4):
            grid2[i] = map(int, f.readline().split(' '))

        ans = solve(answer_1, grid1, answer_2, grid2)
        print('Case #%s: %s'%(str(puzzle_count + 1), ans))
