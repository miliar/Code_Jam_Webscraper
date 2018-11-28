mapping = {
'a': 'y',
'b': 'h',
'c': 'e',
'd': 's',
'e': 'o',
'f': 'c',
'g': 'v',
'h': 'x',
'i': 'd',
'j': 'u',
'k': 'i',
'l': 'g',
'm': 'l',
'n': 'b',
'o': 'k',
'p': 'r',
'q': 'z',
'r': 't',
's': 'n',
't': 'w',
'u': 'j',
'v': 'p',
'w': 'f',
'x': 'm',
'y': 'a',
'z': 'q',
}

n = int(raw_input().strip())
for case in range(n):
    l = raw_input()
    lo = ''
    for j in range(len(l)):
        if l[j] != ' ':
            lo = lo + mapping[l[j]]
        else:
            lo = lo + l[j]
    print 'Case #%d: %s' % (case + 1, lo)
