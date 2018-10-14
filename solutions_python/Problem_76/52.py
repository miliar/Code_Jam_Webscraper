import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))

for k in xrange(T):
    N = int(infile.readline())
    s = map(int,string.split(string.strip(infile.readline())))
    count = 0
    minimum = None
    for n in s:
        count = count ^ n
        if minimum is None:
            minimum = n
        else:
            if n < minimum:
                minimum = n
    answer = 'NO'
    if count == 0:
        answer = sum(s)-minimum

    outfile.write('Case #%d: %s\n' % (k+1,answer))
