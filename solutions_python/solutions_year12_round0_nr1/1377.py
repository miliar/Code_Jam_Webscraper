import string

base = "abcdefghijklmnopqrstuvwxyz"
tran = "ynficwlbkuomxsevzpdrjgthaq"
f = open("input.txt", 'r')
num_lines = int(f.readline().strip())
lines = []
for line in f:
    lines.append(line.strip())
f.close()

trans_table = string.maketrans(tran, base)

f = open("output.txt", 'w')
for i in range(num_lines):
    f.write( "Case #" + str(int(i+1)) +\
            ": " + string.translate(lines[i], trans_table))

    if i != num_lines-1:
        f.write('\n')
f.close()
