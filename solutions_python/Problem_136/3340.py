f = open('b.in', 'r')
fw = open('b.out', 'w')


def timeSpent(n):
    return sum([(C/(r+F*i)) for i in range(n)])

def timeTarget(n):
    return X / (r+F*abs(n))

def totalTime(n):
    return timeSpent(n) + timeTarget(n)

def indexWhen0():
    i = 0
    result = 500
    while True:
        result = totalTime(i)-totalTime(i+1)
        if result <= 0:
            break
        i += 1
    return i

def answer(case):
    r = 2
    C, F, X = case[0], case[1], case[2]
    return totalTime(indexWhen0())


if __name__ == "__main__":
    n = int(f.readline()[:-1])
    case = f.read().split('\n')
    for i in range(n):
        x= tuple(map(float, case[i].split()))
        r, C, F, X = 2, x[0], x[1], x[2]
        fw.write("Case #%d: %.7f\n" % (i+1, answer(x)))

f.close()
fw.close()