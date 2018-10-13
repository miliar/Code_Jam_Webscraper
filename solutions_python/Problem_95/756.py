s = {}

def build(a, b):
    global s
    for i,x in enumerate(a):
        s[x] = b[i]

def solve(string):
    global s
    t = ''

    for x in string:
        if x not in s:
            continue
        else:
            t += s[x]
    return t

def output(N, ans):
    print 'Case #{0}: {1}'.format(N, ans)

def main():
    global s

    build('a', 'y')

    build('o', 'e')

    build('z', 'q')

    build('ejp mysljylc kd kxveddknmc re jsicpdrysi', 
          'our language is impossible to understand')

    build('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'there are twenty six factorial possibilities')

    build('de kr kd eoya kw aej tysr re ujdr lkgc jv',
          'so it is okay if you want to just give up')

    build('q', 'z')

    with open('A-small-attempt0.in', 'r') as f:
        N = int(f.readline())

        for i in xrange(N):
            output(i + 1, solve(f.readline()))

if __name__ == '__main__':
    main() 
