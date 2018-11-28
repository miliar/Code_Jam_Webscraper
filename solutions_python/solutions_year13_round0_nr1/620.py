def winning(l):
    x = l.count('X')
    y = l.count('O')
    t = l.count('T')
    if x == 4 or (x == 3 and t == 1):
        return 'X'
    if y == 4 or (y == 3 and t == 1):
        return 'O'
    return ''

def get_row(l, x):
    return [l[x][0],l[x][1],l[x][2],l[x][3]]

def get_col(l, x):
    return [l[0][x],l[1][x],l[2][x],l[3][x]]

def main():
    lines = open(input(prompt='input')).readlines()
    T = int(lines[0])
    lines = lines[1:5*T+1]

    s = ''
    for i in range(0,len(lines),5):
        case = lines[i:i+4]
        full = ''.join(case).count('.') == 0
        result = 'Case #'+str(i//5 + 1)+': '
        winner = ''
        for j in range(4):
            col = get_col(case, j)
            row = get_row(case, j)
            w = winning(col)
            w2 = winning(row)
            if w != '':
                result += w + ' won'
                break
            if w2 != '':
                result += w2 + ' won'
                break
        else:
            diag = [case[0][0], case[1][1], case[2][2], case[3][3]]
            diag2 = [case[0][3], case[1][2], case[2][1], case[3][0]]
            w = winning(diag)
            w2 = winning(diag2)
            if w != '':
                result += w + ' won'
            elif w2 != '':
                result += w2 + ' won'
            elif full:
                result += 'Draw'
            else:
                result += 'Game has not completed'
        s += result + '\n'
    open(input(prompt='output'), 'w').write(s)

if __name__ == '__main__':
    main()