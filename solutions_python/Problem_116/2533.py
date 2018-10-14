file = open('A-large.in', 'r')
output = open('problem_solve.txt', 'w')

VALUES = {
    'T': 10,
    'X': 1,
    'O': 0,
    '.': -100
}

winx = [4, 31, 22, 13]
diagonal_1 = [(0,3), (1,2), (2,1), (3,0)]
diagonal_2 = [(0,0), (1,1), (2,2), (3,3)]


def check_val(val, invalid):
    if val < 0:
        return 0, invalid + 1
    elif val == 0 or val%10 == 0:
        return 'Case #%d: O won\n', invalid
    elif val in winx:
        return 'Case #%d: X won\n', invalid
    else:
        return 0, invalid

def check_line(lin, tab, invalid, counter):
    val = 0
    for a in range(len(lin)):
        b = VALUES[lin[a]]
        val += b
        tab[a] += b
        if (counter, a) in diagonal_1:
            tab[4] += b
        elif (counter, a) in diagonal_2:
            tab[5] += b
    res, invalid = check_val(val, invalid)
    return tab, res, invalid


tab = [0, 0, 0, 0, 0, 0]
first = True
numb = 0
counter = 0

numb = int(file.readline().strip())
num = 1
winer = 0
invalid = 0
counter = 0

for line in file:
    lin = line.strip()
    if lin:
        
        if not winer:
            tab, res, invalid = check_line(lin, tab, invalid, counter)
            if res:
                winer = 1
                output.write(res % num)
                res = 0
        counter += 1
    else:
        if not winer:
            for x in tab:
                if not winer:
                    res, invalid = check_val(x, invalid)
                    if res:
                        output.write(res % num)
                        winer = 1
                        res = 0
        if not winer and invalid > 0:
            output.write('Case #%d: Game has not completed\n' % num)
        elif not winer:
            output.write('Case #%d: Draw\n' % num)
        tab = [0, 0, 0, 0, 0, 0]
        invalid = 0
        winer = 0
        counter = 0
        num += 1

output.close()