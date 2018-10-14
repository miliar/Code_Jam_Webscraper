from numpy import *

def make_matrix(f):
    matrix = []
    for i in range(4):
        row = [int(x) for x in f.readline().strip().split()]
        matrix.append(row)

    return array(matrix).reshape(4,4)

def parse_stuff(f, w, num):
    count = 1
    while count <= num:
        guess = int(f.readline().strip())
        result1 = make_matrix(f)
        guess2 = int(f.readline().strip())
        result2 = make_matrix(f)


        row1 = result1[guess-1]
        row2 = result2[guess2-1]
        
        ans = []

        for i in row1:
            for j in row2:
                if i == j:
                    ans.append(i)

        if not ans:
            w.write('Case #%d: Volunteer cheated!\n' % count)
        elif len(ans) > 1:
            w.write('Case #%d: Bad magician!\n' % count)
        else:
            w.write('Case #%d: %d\n' % (count, ans[0]))

        count += 1

with open('A-small-attempt1.in', 'r') as f, open('result1.txt', 'w') as w:
    line = f.readline()
    num_of_tests = int(line.strip())
    parse_stuff(f, w, num_of_tests)
