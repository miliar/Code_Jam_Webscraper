infile = 'B-large.in'
outfile = 'Blarge-out.txt'

f = open(infile, 'r')
out = open(outfile, 'w')
T = int(f.readline())

for m in range(T):

    C,F,X = map(float, f.readline().split())

    a = 0.
    t = 0.
    r = 2.

    while True:
        w = X/r
        x = C/r+X/(r+F)
        if(w>x):
            a+=1
            t+=C/r
            r+=F
        else:
            t+=X/r
            break
    print a,t,r

    out.write('Case #'+str(m+1)+': ')
    out.write(str(t))

    out.write('\n')

out.close()
