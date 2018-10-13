f = open('A-small-attempt0.in', 'r')
o = open('MagicTrick.out', 'w')

N = int(f.readline())
MagicTricks = []
for x in range(N):
    sublist = []
    sublist.append(int(f.readline()))
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append(int(f.readline()))
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    sublist.append([int(k) for k in f.readline().split(' ')])
    MagicTricks.append(sublist)

def compare(row1, row2):
    count = 0
    for x in row1:
        if x in row2:
            count += 1
    if count == 1:
        for x in row1:
            if x in row2:
                return str(x)
    elif count == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'
    

def get_row(MagicTrick):
    return MagicTrick[MagicTrick[0]], MagicTrick[MagicTrick[5]+5]

answers = []

for x in MagicTricks:
    answers.append(compare(get_row(x)[0], get_row(x)[1]))

for x in range(N):
    o.write('Case #' + str(x+1) + ': ' + answers[x] + '\n')



