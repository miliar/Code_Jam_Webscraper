__author__ = 'Glen'
numCases = int(input().strip())
for caseNum in range(numCases):
    chosen = []
    row = int(input().strip()) - 1
    for i in range(4):
        cards = list(map(int, input().strip().split()))
        if i == row:
            chosen.extend(cards)
    row = int(input().strip()) - 1
    for i in range(4):
        cards = list(map(int, input().strip().split()))
        if i == row:
            chosen = list(filter(lambda c: c in chosen, cards))
    base = 'Case #{}: '.format(caseNum+1)
    if len(chosen) == 0:
        print(base + 'Volunteer cheated!')
    elif len(chosen) == 1:
        print(base + str(chosen.pop()))
    elif len(chosen) > 1:
        print(base + 'Bad magician!')