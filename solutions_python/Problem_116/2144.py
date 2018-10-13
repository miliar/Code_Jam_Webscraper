def check_fours(fours):
    for four in fours:
        normalized_four = four.replace('T', 'X')
        #print 'four:', four
        #print 'normalized_four:', normalized_four
        if normalized_four.count("X") == 4:
            return "X won"
        normalized_four = four.replace('T', 'O')
        if normalized_four.count("O") == 4:
            return "O won"

def get_cols(rows):
    result = ['', '', '', '']
    for row in rows:
        for i, s in enumerate(row):
            result[i] += s
    #print  rows, 'cols:', result
    return result

def decide(rows):     
    result = check_fours(rows)
    if result:
        return result
    result = check_fours(get_cols(rows))
    if result:
        return result
    result = check_fours(get_diags(rows))
    if result:
        return result
    if is_done(rows):
        return "Draw"
    else:
        return "Game has not completed"

def is_done(rows):
    for row in rows:
        if '.' in row:
            return False
    return True

def get_diags(rows):
    d = ''
    d2 = ''
    for i in range (4):
        d += rows[i][i]
        d2 += rows[i][3 - i]
    #print  rows, [d, d2] 
    return [d, d2]
    
filename = 'A-small-attempt0.in'
f = open(filename)
o = open('solution.out', 'w')

n = int(f.readline().strip())

count = 1
rows = []
for line in f.readlines():
    line = line.strip()
    if len(line) == 0:
        o.write("Case #" + str(count) + ": " + decide(rows))
        count += 1
        if count <= n:
            o.write('\n')
        rows = []
    else:
        rows.append(line)
f.close()
o.close()
