with open('D-large.in', 'r') as a:
    text = a.readlines()
    a.close()
b = open('D-large.out', 'w+')
cases = int(text[0])

def war(x, y):
    x_score = 0
    y_score = 0
    while len(x) > 0 and len(y) > 0:
        a = x.pop(0)
        b = 0
        for block in y:
            if block > a:
                b = y.pop(y.index(block))
                break
        if b == 0:
            b = y.pop(0)
        if a > b:
            x_score += 1
        else:
            y_score += 1
    return [x_score, y_score]

for i in range(0, cases):
    b.write("Case #{}: ".format(i + 1))
    blocks = text[i * 3 + 1]
    naomi = text[i * 3 + 2].split()
    ken = text[i * 3 + 3].split()
    naomi.sort()
    ken.sort()
    nblocks = []
    kblocks = []
    for block in naomi:
        nblocks.append(float(block))
    for block in ken:
        kblocks.append(float(block))
    b.write(str(war(kblocks, nblocks)[1]) + " ")
    for block in naomi:
        nblocks.append(float(block))
    for block in ken:
        kblocks.append(float(block))
    b.write(str(war(nblocks, kblocks)[0]) + "\n")
b.close()