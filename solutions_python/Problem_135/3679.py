t = int(raw_input())
for i in range(t):
    first = int(raw_input()) - 1
    cards_one = []
    for j in range(4):
        cards_one.append([int(x) for x in raw_input().split(' ')])
    second = int(raw_input()) - 1
    cards_two = []
    for j in range(4):
        cards_two.append([int(x) for x in raw_input().split(' ')])
    r = [x for x in cards_one[first] if x in cards_two[second]]
    output = ''
    if len(r) == 0:
        output = 'Volunteer cheated!'
    elif len(r) == 1:
        output = r[0]
    else:
        output = 'Bad magician!'
    print 'Case #' + str(i+1) + ': ' + str(output)