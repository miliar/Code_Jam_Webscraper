draw = "Draw"
notcompleted = "Game has not completed"

def score(a):
    def won(c):
        return c + " won"
    for a in (a, zip(*a)):
        for x in ('X', 'O'):
            if any(all(z in [x, "T"] for z in y) for y in a):
                return won(x)
    for a in (a, list(reversed(a))):
        for x in ('X', 'O'):
           if all(c[n] in [x, "T"] for n, c in enumerate(a)):
                return won(x)
    if any(any(x == "." for x in y) for y in a):
        return notcompleted
    else:
        return draw

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        g = [[c for c in list(raw_input())] for x in xrange(4)] 
        raw_input()
        r = score(g)
        print "Case #%d: %s" % (t, r)

if __name__ == '__main__':
    main()
