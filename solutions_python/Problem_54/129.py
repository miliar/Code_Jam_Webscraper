
ilist = []
def ri():
    global ilist
    if ilist:
        return ilist.pop(0)
    else:
        while not ilist:
            ilist = [int(s) for s in raw_input().split()]
        return ri()

def main():
    for i in range(ri()):
        solve(i+1)

def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a%b)


def solve(t):
    n = ri()
    a = ri()

    b = abs(ri() - a)
    for i in range(n-2):
        b = nwd(b, abs(ri() - a))

    print 'Case #%d: %d' % (t, (b - a % b) % b)

main()
