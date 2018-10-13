from sys import stdout


def answer(smax, audience):
    r = 0
    count = 0
    target = 0
    for i in range(0, smax + 1):
        count += audience[i]
        if count >= smax:
            break
        target = count
        if i < target:
            continue
        r += 1
        count += 1
    return r

with open('A-large.in', 'r') as f:
    stdout = open('A-large-out', 'w')
    T = int(f.readline())
    for i in range(1, T + 1):
        smax, audience = f.readline().split()
        r = answer(int(smax), list(map(int, audience)))
        stdout.write('Case #%s: %s\n' % (str(i), str(r)))
    stdout.close()
