f = open('A-large.in')

c = int(f.readline())

result = []

def flip(cake):
    return '+' if cake == '-' else '-'

def is_happy(cakes):
    return all(cake == '+' for cake in cakes)

for case in range(c):
    ipt = f.readline().rstrip()
    ipt = ipt.split()
    cakes = list(map(lambda x: x, ipt[0]))
    flipper = int(ipt[1])

    counter = 0
    for i in range(len(ipt[0]) - flipper + 1):
        if cakes[i] == '-':
            for j in range(flipper):
                cakes[i + j] = flip(cakes[i + j])
            counter += 1

    if is_happy(cakes):
        result.append('Case #' + str(case + 1) + ': ' + str(counter) + '\n')
    else:
        result.append('Case #' + str(case + 1) + ': ' + str('IMPOSSIBLE') + '\n')

out = open('A-large.out', 'w')
for l in result:
    out.writelines(l)