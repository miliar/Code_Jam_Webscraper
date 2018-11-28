__author__ = 'cdong'

def getAnswer(c, f, x):
    rate = 2

    if (c > x):
        return x/rate

    time = c/rate

    while ( ((x - c) * (rate + f)) > (x * rate)):
        rate += f
        time += c/rate

    time += (x - c)/rate

    return time

def solve(test, fin):
    l = fin.readline()
    # print(l)
    c, f, x = l.split()
    answer = getAnswer(float(c), float(f), float(x))
    print("Case #%d: %.8f" % (test, answer))

# fin = open('input.txt')
fin = open('/Users/cdong/Downloads/B-large.in')
noTests = int(fin.readline())
for i in range(noTests):
    solve(i + 1, fin)