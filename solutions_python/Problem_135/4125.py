input = map(lambda x: x[:-1], list(open('input.txt'))[1:])

tricks = []

while input:
    tricks.append(
        [
            {
                'row': int(input[0]),
                'cards': tuple([tuple(row.split()) for row in input[1:5]])
            },
            {
                'row': int(input[5]),
                'cards': tuple([tuple(row.split()) for row in input[6:10]])
            }
        ]
    )
    for item in input[:10]:
        input.remove(item)

for trick_num, trick in enumerate(tricks):
    for cards_num, cardset in enumerate(trick):
        trick[cards_num] = set(cardset['cards'][cardset['row'] - 1])
    possible_answers = trick[0] & trick[1]
    if len(possible_answers) < 1:
        result = 'Volunteer cheated!'
    elif len(possible_answers) == 1:
        result = possible_answers.pop()
    elif len(possible_answers) > 1:
        result = 'Bad magician!'

    print 'Case #%s: %s' % (trick_num + 1, result)