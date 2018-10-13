f = open("data.txt")
g = open("data1.txt", 'w')

def win(x, y):
    a = max(x, y)
    b = min(x, y)
    if b == 0:
        return 1
    elif a == b:
        return 0
    elif a % b == 0:
        return 1
    else:
        j = a // b
        for l in range(j, 0, -1):
            if win(a-(l*b), b) == 0:
                return 1
                break
        else:
            return 0
    
for i, line in enumerate(f):
    if i == 0:
            continue
    c = 0
    a1, a2, b1, b2 = (int(x) for x in line.split())
    for a in range(a1, a2 + 1):
        for b in range(b1, b2 + 1):
            if win(a, b) == 1:
                c += 1
    string = 'Case #' + str(i) + ': ' + str(c) + '\n'
    g.write(string)
