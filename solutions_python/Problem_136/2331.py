import sys

def make_cookie(c, f, x):
    speed = 2.0
    s = 0

    while True:
        if (c/speed + x/(speed+f)) > x/speed:
            s += x/speed
            break
        s += c/speed
        speed += f
    return s


fn = sys.argv[1]

f = open(fn)
tls = f.read().split('\n')

count = int(tls[0])

i = 1

case_i = 1

for row in tls[1:]:
    if not row:
        continue
    c, f, x = map(float, row.split(' '))
    s = make_cookie(c, f, x)
    print "Case #%s:" % case_i,
    print "%0.7f" % s
    case_i += 1
