import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))


for k in xrange(T):
    N = int(infile.readline())
    s = map(int,string.split(string.strip(infile.readline())))
    count = 0
    for (a,b) in zip(s,range(len(s))):
        if a != b+1:
            count += 1    
    answer = count

    outfile.write('Case #%d: %s\n' % (k+1,answer))

