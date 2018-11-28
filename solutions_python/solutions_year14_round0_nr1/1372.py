import sys

inp = sys.stdin
get_int = lambda: int(inp.readline())
get_ints = lambda: map(int, inp.readline().split())

T = get_int()
for case_number in range(1, T + 1):
    answer1 = get_int()
    arrangement1 = [get_ints() for _ in range(4)]
    answer2 = get_int()
    arrangement2 = [get_ints() for _ in range(4)]
    card = set(arrangement1[answer1 - 1]) & set(arrangement2[answer2 - 1])
    if len(card) == 1:
        out = card.pop()
    elif not card:
        out = 'Volunteer cheated!'
    else:
        out = 'Bad magician!'
    print 'Case #%d: %s' % (case_number, out)
