mapping = {'a': 'y', 'o': 'e', 'z': 'q', 'q': 'z'}

def train():
    a = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

    b = ["our language is impossible to understand",
         "there are twenty six factorial possibilities",
         "so it is okay if you want to just give up"]

    remaining_i = set("abcdefghijklmnopqrstuvwxyz")
    remaining_o = set("abcdefghijklmnopqrstuvwxyz")

    for i in range(3):
        for (j, c) in enumerate(a[i]):
            mapping[c] = b[i][j]
            remaining_i.difference_update({c})
            remaining_o.difference_update({b[i][j]})

def solve(g):
    return ''.join(mapping.get(c, c) for c in g)

if __name__ == '__main__':
    train()
    T = int(raw_input())
    for X in range(1, T+1):
        G = raw_input()
        S = solve(G)
        print "Case #%d: %s" % (X, S)

