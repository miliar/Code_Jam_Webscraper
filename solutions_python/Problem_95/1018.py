mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z','z':'q'}
fi=open('A-small-attempt0.in','r')
fo=open('tout.txt','w')
t=int(fi.readline())
for i in range(t):
    g=fi.readline().strip('\n')
    output = ''
    for c in g:
        if c in g:
            output+=mapping[c]
        else:
            output+=c
    fo.write('Case #%d: %s\n'%(i+1,output))

fo.close()
