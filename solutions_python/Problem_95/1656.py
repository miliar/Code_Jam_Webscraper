def map(in_char):
    out = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz \n'
    goog =  'ynficwlbkuomxsevzpdrjgthaq \n'
    for ch in in_char[:]:
        ind = goog.index(ch)
        out = out+alpha[ind]
    return out

f = open('input', 'r')
t = int(f.readline())
for n in range(t):
    inp = f.readline()
    print('Case #'+str(n+1)+': '+map(inp[:-1]))
f.close();
