N = int(raw_input())

s = "welcome to code jam"
ls = len(s)

def clean(text):
    return [c for c in text if c in s]

def make_tab(text):
    tab = {}
    for c in s:
        tab[c] = []

    for i, c in enumerate(text):
        tab[c].append(i)
    return tab

def step(tab, si, i):
    if si == ls - 1:
        return 1
    else:
        nexti = si + 1
        next = s[nexti]
        count = 0
        for ind in tab[next]:
            if ind < i:
                continue
            count += step(tab, nexti, ind)
        return count

def recurse(tab):
    count = 0
    for i in tab[s[0]]:
        count += step(tab, 0, i)
    return count

def out(text):
    text = clean(text)
    tab = make_tab(text)
    return recurse(tab) % 10000

for i in xrange(N):
    text = raw_input()
    print 'Case #%d: %04d' % (i + 1, out(text))
