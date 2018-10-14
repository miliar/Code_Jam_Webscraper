def tidify(n):
    for i in range(2, len(n)):
        if int(n[len(n) - i]) < int(n[len(n) - i - 1]):
            n[len(n) - i:-1] = ['9' for x in n[len(n) - i:-1]]
            n[len(n) - i - 1] = str(int(n[len(n) - i - 1]) - 1)
            if int(n[len(n) - i - 1]) < 0:
                n[len(n) - i - 1] = '9'
    if n[0] == '0':
        n = n[1:]
    return n


i = open('B-large.in', 'r')
o = open('solution.out', 'w')
it = 0
for line in i:
    if it:
        o.write('Case #' + str(it) + ': ')
        n = list(line)
        for digit in tidify(n):
            o.write(digit)
    it += 1
