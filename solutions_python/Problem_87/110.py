import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))


for k in xrange(T):
    #N = int(infile.readline())
    s = map(int,string.split(string.strip(infile.readline())))
    X, S, R, t, N = s[0], s[1], s[2], s[3], s[4]
    length_at_speed = [0 for a in range(201)]
    for i in range(N):
        line = map(int,string.split(string.strip(infile.readline())))
        length_at_speed[line[2]+S] += line[1]-line[0]
    length_at_speed[S] = X - sum(length_at_speed)
    for j in range(201):
        if length_at_speed[j] > 0:
            print "length at speed %d: %f" % (j,length_at_speed[j])
    time_spent = 0
    for j in range(201):
        if length_at_speed[j] > 0:
            if t < length_at_speed[j] / float(j+R-S):
                time_spent += t
                time_spent += (length_at_speed[j] - t * float(j+R-S)) / float(j)
                t = 0
            else:
                time_spent += (length_at_speed[j]) / float(j+R-S)
                t -= (length_at_speed[j]) / float(j+R-S)
    answer = time_spent

    outfile.write('Case #%d: %s\n' % (k+1,answer))

