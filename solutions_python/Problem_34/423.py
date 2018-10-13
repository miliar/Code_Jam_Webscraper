import sys


def parse_token(token):
    res = []
    gr = False
    tmp = []

    for c in token:
        if c == '(':
            gr = True
        elif c == ')':
            gr = False
        else:
            tmp.append(c)

        if not gr:
            res.append(tmp)
            tmp = []

    return res


def parse_input(file):  # ((L, D, N), words, tokens)
    L, D, N = map(int, file.readline().split())
    
    words = [file.readline()[:-1] for i in xrange(D)]



    tokens = [parse_token(file.readline()[:-1]) for i in xrange(N)]

    return ((L, D, N), words, tokens)


def match_token(word, token):
    for n, c in enumerate(word):
        if c not in token[n]:
            return False
    else:
        return True


def main():
    fnames = sys.argv[1:3]
    inp = open(fnames[0], 'rt')
    outp = open(fnames[1], 'wt')

    (L, D, N), words, tokens = parse_input(inp)
    inp.close()

    for n, token in enumerate(tokens):
        i = 0
        for word in words:
            if match_token(word, token):
                i += 1
        outp.write('Case #%d: %d\n' % (n+1, i))
        print n

    outp.close()


if __name__ == '__main__':
    main()

