f = open('B-large.in')
r = open('out.txt', 'w')

def check_lawn(lawn):
    lawnT = [list(x) for x in zip(*lawn)]
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            if max(lawn[i]) > lawn[i][j] and max(lawnT[j]) > lawn[i][j]:
                return 'NO'
    return 'YES'

n = int(f.readline().strip())
for i in range(n):
    h, w = tuple(int(x) for x in f.readline().strip().split())
    lawn = []
    for j in range(h):
        lawn.append([int(x) for x in f.readline().strip().split()])
    print check_lawn(lawn)
    r.write('Case #' + str(i+1) + ': ' + check_lawn(lawn) + '\n')

f.close()
r.close()
