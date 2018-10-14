fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

mas1 = [(1, 1, 1, 'GABRIEL'), (1, 1, 2, 'GABRIEL'), (1, 1, 3, 'GABRIEL'), (1, 1, 4, 'GABRIEL'), (1, 2, 1, 'GABRIEL'), (1, 2, 2, 'GABRIEL'), (1, 2, 3, 'GABRIEL'), (1, 2, 4, 'GABRIEL'), (1, 3, 1, 'GABRIEL'), (1, 3, 2, 'GABRIEL'), (1, 3, 3, 'GABRIEL'), (1, 3, 4, 'GABRIEL'), (1, 4, 1, 'GABRIEL'), (1, 4, 2, 'GABRIEL'), (1, 4, 3, 'GABRIEL'), (1, 4, 4, 'GABRIEL'), (2, 1, 1, 'RICHARD'), (2, 1, 2, 'GABRIEL'), (2, 1, 3, 'RICHARD'), (2, 1, 4, 'GABRIEL'), (2, 2, 1, 'GABRIEL'), (2, 2, 2, 'GABRIEL'), (2, 2, 3, 'GABRIEL'), (2, 2, 4, 'GABRIEL'), (2, 3, 1, 'RICHARD'), (2, 3, 2, 'GABRIEL'), (2, 3, 3, 'RICHARD'), (2, 3, 4, 'GABRIEL'), (2, 4, 1, 'GABRIEL'), (2, 4, 2, 'GABRIEL'), (2, 4, 3, 'GABRIEL'), (2, 4, 4, 'GABRIEL'), (3, 1, 1, 'RICHARD'), (3, 1, 2, 'RICHARD'), (3, 1, 3, 'RICHARD'), (3, 1, 4, 'RICHARD'), (3, 2, 1, 'RICHARD'), (3, 2, 2, 'RICHARD'), (3, 2, 3, 'GABRIEL'), (3, 2, 4, 'RICHARD'), (3, 3, 1, 'RICHARD'), (3, 3, 2, 'GABRIEL'), (3, 3, 3, 'GABRIEL'), (3, 3, 4, 'GABRIEL'), (3, 4, 1, 'RICHARD'), (3, 4, 2, 'RICHARD'), (3, 4, 3, 'GABRIEL'), (3, 4, 4, 'RICHARD'), (4, 1, 1, 'RICHARD'), (4, 1, 2, 'RICHARD'), (4, 1, 3, 'RICHARD'), (4, 1, 4, 'RICHARD'), (4, 2, 1, 'RICHARD'), (4, 2, 2, 'RICHARD'), (4, 2, 3, 'RICHARD'), (4, 2, 4, 'RICHARD'), (4, 3, 1, 'RICHARD'), (4, 3, 2, 'RICHARD'), (4, 3, 3, 'RICHARD'), (4, 3, 4, 'GABRIEL'), (4, 4, 1, 'RICHARD'), (4, 4, 2, 'RICHARD'), (4, 4, 3, 'GABRIEL'), (4, 4, 4, 'GABRIEL')]
t = int(fin.readline())
for test in range(1, t + 1):
    x, r, c = map(int, fin.readline().split())
    for elem in mas1:
        if elem[0] == x and elem[1] == r and elem[2] == c:
            fout.write('Case #' + str(test) + ': ' + elem[3] + '\n')
fin.close()
fout.close()
