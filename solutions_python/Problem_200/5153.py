fin = open('B-small.in')
fout = open('B-small.out', 'w')
t = int(fin.readline().strip())


def is_okay(v):
    lv = list(str(v))
    for i in range(len(lv)-1):
        if int(lv[i]) > int(lv[i+1]):
            return False
    return True


for tc in range(t):
    n = int(fin.readline().strip())

    while not is_okay(n):
        n -= 1

    fout.write("Case #{}: {}\n".format(tc+1, n))

