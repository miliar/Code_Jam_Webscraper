
def check_lawn(lawn, reverse_lawn):
    for i in range(x):
        for j in range(y):
            p = lawn[i][j]

            hor = lawn[i][:j] + lawn[i][j + 1:]
            ver = reverse_lawn[j][:i] + reverse_lawn[j][i + 1:]

            if not all(map(lambda item: item <= p, hor)) and not all(map(lambda item: item <= p, ver)):
                return 'NO'

    return 'YES'


NN = int(raw_input())

for CC in range(NN):
    x, y = map(int, raw_input().strip().split())
    
    lawn = []
    reverse_lawn = [[] for i in range(y)]
    for i in range(x):
        row = raw_input().strip().split()
        lawn.append(row)
        for i, p in enumerate(row):
            reverse_lawn[i].append(p)

    print 'Case #{}:'.format(CC + 1), check_lawn(lawn, reverse_lawn)
