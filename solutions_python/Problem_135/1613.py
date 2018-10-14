import sys
lines = open(sys.argv[1]).read().splitlines()
fp = open('OUTPUT.txt', 'w')

num_cases = int(lines.pop(0))
for case in range(num_cases):
    cards = []
    for guess in range(2):
        row = int(lines.pop(0))
        for i in range(4):
            line = lines.pop(0)
            if i + 1 == row:
                # this is the expected row
                cards.append(set(line.split()))

    overlap = cards[0] & cards[1]
    num_solutions = len(overlap)
    if len(overlap) == 0:
        result = 'Volunteer cheated!'
    elif len(overlap) == 1:
        result = overlap.pop()
    else:
        result = 'Bad magician!'
    fp.write('Case #{}: {}\n'.format(case + 1, result))

fp.close()
