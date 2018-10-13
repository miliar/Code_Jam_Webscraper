
fin = open('A-large.in')
fout = open('A.out.txt', 'w')

T = int(next(fin))

def win(data):
    yield from (data[i*4:i*4+4] for i in range(4))
    yield from (data[i::4] for i in range(4))
    yield (
        data[0+0]+
        data[1+4]+
        data[2+8]+
        data[3+12]
    )
    yield (
        data[3+0]+
        data[2+4]+
        data[1+8]+
        data[0+12]
    )

def solve(f):
    data = ''.join(f.read(21).split())
    dataO = data.replace('T', 'O')
    dataX = data.replace('T', 'X')
    for i in win(dataO):
        if i=='OOOO':
            return 'O won'
    for i in win(dataX):
        if i=='XXXX':
            return 'X won'
    if '.' in data:
        return "Game has not completed"
    return 'Draw'

for i in range(1, T+1):
    print("Case #{}:".format(i), solve(fin), file=fout)

fout.close()
