import sys

if len(sys.argv) != 3:
    print("Usage: python scriptA.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'sampleA.in'
#output_file = 'sampleA.out'

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for c in xrange(0,T):
        horiz = [0,0,0,0]
        h_tomek = [0,0,0,0]
        vert = [0,0,0,0]
        v_tomek = [0,0,0,0]
        diag = [0,0]
        diag_tomek = [0,0]
        empty = 0
        x_lines = 0
        o_lines = 0

        for row in xrange(0,4):
            line = f.readline()
            for col in xrange(0,4):
                if line[col] == '.': empty += 1
                elif line[col] == 'X':
                    horiz[row] += 1
                    vert[col] += 1
                    if row == col: diag[0] += 1
                    elif row + col + 1 == 4: diag[1] += 1
                elif line[col] == 'O':
                    horiz[row] -= 1
                    vert[col] -= 1
                    if row == col: diag[0] -= 1
                    elif row + col + 1 == 4: diag[1] -= 1
                elif line[col] == 'T':
                   h_tomek[row] = 1
                   v_tomek[col] = 1
                   if row == col: diag_tomek[0] = 1
                   elif row + col + 1 == 4: diag_tomek[1] = 1
        line = f.readline()

        for i in xrange(0,4):
            if horiz[i] > 0: horiz[i] += h_tomek[i]
            elif horiz[i] < 0: horiz[i] -+ h_tomek[i]

            if vert[i] > 0: vert[i] += v_tomek[i]
            elif vert[i] < 0: vert[i] += v_tomek[i]

            if i < 2 and diag[i] > 0: diag[i] += diag_tomek[i];
            elif i < 2 and diag[i] < 0: diag[i] -= diag_tomek[i];

        x_lines = horiz.count(4) + vert.count(4) + diag.count(4)
        o_lines = horiz.count(-4) + vert.count(-4) + diag.count(-4)
        results.append('Case #' + str(c+1) + ': ')
        if x_lines == o_lines:
            if empty > 0: results[c] += 'Game has not completed\n'
            else: results[c] += 'Draw\n'
        elif x_lines > o_lines: results[c] += 'X won\n'
        else: results[c] += 'O won\n'

with open(output_file, 'w') as f:
        f.writelines(results)



