output = []
with open('A-small-attempt0.in.txt') as f:
    T = int(f.readline().split()[0])
    for i in xrange(T):
        first = int(f.readline().split()[0])
        for j in xrange(first - 1):
            f.readline()
        cards1 = [x for x in f.readline().split()]
        for j in xrange(4 - first):
            f.readline()
            
        second = int(f.readline().split()[0])
        for j in xrange(second - 1):
            f.readline()
        cards2 = [x for x in f.readline().split()]
        for j in xrange(4 - second):
            f.readline()
            
        card = [card for card in cards1 if card in cards2]
        if len(card) == 0:
            output += ['Case #' + str(i + 1) + ': Volunteer cheated!']
        elif len(card) == 1:
            output += ['Case #' + str(i + 1) + ': ' + card[0]]
        else:
            output += ['Case #' + str(i + 1) + ': Bad magician!']

with open('output.txt', 'w') as f:
    f.write('\n'.join(output))