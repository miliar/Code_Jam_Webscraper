#%%
file_ = open('input')
test_cases = int(file_.readline())

#%%
def read_row(rows):
    answer = int(file_.readline()) - 1
    for i in range(4):
        if i == answer:
            rows.append([int(item) for item in file_.readline().split()])
        else:
            next(file_)

#%%
output_file = open('output', 'w')
for test_case in range(test_cases):
    output_file.write('Case #{}: '.format(test_case + 1))
    rows = []
    for i in range(2):
        read_row(rows)
    cards = []
    for i in range(4):
        for j in range(4):
            if rows[0][i] == rows[1][j]:
                cards.append(rows[0][i])
    if not cards:
        output_file.write('Volunteer cheated!\n')
    elif len(cards) > 1:
        output_file.write('Bad magician!\n')
    else:
        output_file.write('{}\n'.format(cards[0]))