f = open('A-large.in')
L, D, N = (int(x) for x in f.readline().split())
dicts = [{} for x in range(L)]
words = set()
for n in range(D):
    word = f.readline().strip()
    words.add(word)
    for i in range(L):
        if not word[i] in dicts[i]:
            dicts[i][word[i]] = set()
        dicts[i][word[i]].add(word)

for n in range(N):
    posss = words.copy()
    word = f.readline()
    for i in range(L):
        if word[0] == '(':
            close = word.find(')')
            opts = word[1:close]
            word = word[close+1:]
        else:
            opts = word[0]
            word = word[1:]
        optss = [dicts[i].get(opt, set()) for opt in opts]
        posss.intersection_update(reduce(lambda a, b: a.union(b), optss))
    print "Case #%s: %s" % (n + 1, len(posss))
