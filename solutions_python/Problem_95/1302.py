decrypt_dict = {
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q',
    ' ' : ' '
}

def decrypt(text):
    text = text.replace('\n', '')
    result = ''
    for c in text:
        result += decrypt_dict[c]
    return result

f = open('A-small-attempt0.in')
N = int(f.readline())
for i in range(N):
    print 'Case #%d: %s' % (i+1, decrypt(f.readline()))
f.close()
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# our language is impossible to understand
#
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# there are twenty six factorial possibilities
#
# de kr kd eoya kw aej tysr re ujdr lkgc jv
# so it is okay if you want to just give up
