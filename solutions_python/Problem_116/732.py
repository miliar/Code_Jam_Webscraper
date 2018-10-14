def tic(input):
    for i in range(4):
        input.append([input[j][i] for j in range(4)])
    input.append([input[j][j] for j in range(4)])
    input.append([input[j][3-j] for j in range(4)])
    dot = 0
    t = 0
    for line in input:
        if '.' in line:
            dot = 1
            continue
        elif 'X' not in line:
            return 'O won'
        elif 'O' not in line:
            return 'X won'
    return 'Game has not completed' if dot == 1 else 'Draw'

if __name__ == '__main__':
    f = open('A-large.in')
    o = open('A-large.out', 'w')
    n = int(f.readline())
    for i in range(n):
        input = []
        for j in range(4):
            input.append(f.readline().strip())    
        o.write('Case #%d: %s\n'%(i+1, tic(input)))
        f.readline()
    o.close()
    f.close()
