T = int(input())

def line():
    answer = int(input())
    for r in range(4):
        if answer == r + 1:
            line = map(int, input().split(' '))
        else:
            input()
    return set(line)

for t in range(1, T + 1):
    answers = line() & line()
    answerLength = len(answers)
    if answerLength == 0:
        print('Case #%d: Volunteer cheated!' % (t,))
    elif answerLength == 1:
        print('Case #%d: %d' % (t, answers.pop()))
    else:
        print('Case #%d: Bad magician!' % (t,))
