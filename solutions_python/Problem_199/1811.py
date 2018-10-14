def solve(row, k):
    row_len, nb_steps = len(row), 0
    for i in range(row_len-k+1):
        if row[i] == '-':
            flip(row, i, k)
            nb_steps += 1
    found = False
    for i in range(row_len):
        if row[i] != '+':
            return "IMPOSSIBLE"
    return nb_steps

file = open('gj_data1_small', 'r')
data = file.read().split('\n')
nb_tests = int(data[0])
for i in range(1, nb_tests+1):
    row, k = data[i].split(' ')
    res = solve(list(row), int(k))
    print 'Case #%s: %s' % (i, res)
