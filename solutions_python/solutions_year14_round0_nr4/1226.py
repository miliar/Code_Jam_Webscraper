from sys import stdin
readline = stdin.readline
def optimal(a, b):
    a = sorted(a)
    b = sorted(b)
    score = 0
    for itema in a:
        if b[0] < itema:
            # a can win with itema
            score += 1
            b.pop(0)
        else:
            # a can't win with itema
            b.pop(-1)
    return score
def b_best(b, amass):
    choice = 0
    for item in b:
        if item > amass:
            choice = item
            break
#    print b, amass, choice
    return choice

def play(a, b):
#    random.shuffle(a)
    b = sorted(b)
    score = 0
    for item in a:
        choice = b_best(b, item)
        score += 1 if choice < item else 0
        if choice > 0:
            b.remove(choice)
    return score
def solve():
    n = int(readline())
    naomi = map(float, readline().split())
    ken = map(float, readline().split())
    return optimal(naomi, ken), play(naomi, ken)

c = int(readline())
for i in range(c):
    m, n = solve()
    print "Case #%d: %d %d" % (i+1, m, n)
