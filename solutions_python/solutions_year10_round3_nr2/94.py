import math
f = open("data.txt")
g = open("data1.txt", 'w')

def count(l, p, c):
    if c*l >= p:
        return 0
    else:
        u = (math.ceil(math.log((p/l), c))) - 1
        v = (math.floor(math.log(u, 2))) + 1
        return v

for i, line in enumerate(f):
    if i == 0:
            continue
    l, p, c = (int(x) for x in line.split())
    stri = str(count(l, p, c))
    string = 'Case #' + str(i) + ': ' + stri + '\n'
    g.write(string)
    print(string)
