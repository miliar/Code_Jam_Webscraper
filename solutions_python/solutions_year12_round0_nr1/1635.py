def make_dict():
    a = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''


    b = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

    a = a.split('\n')
    b = b.split('\n')

    d = {'q': 'z', 'z': 'q'}

    for i, s in enumerate(a):
        for j, c in enumerate(s):
            d[c] = b[i][j]
    
    return d

d = make_dict()

def translate(s):
    r = [d[c] for c in s]
    return ''.join(r)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = raw_input()
        print 'Case #%s:' % (i+1), translate(s)
    
