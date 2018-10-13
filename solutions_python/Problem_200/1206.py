#f_in = open('B.in', 'r')
#f_in = open('B-small-attempt0.in', 'r')
f_in = open('B-large.in', 'r')
#f_out = open('B.out', 'w')
#f_out = open('B-small.out', 'w')
f_out = open('B-large.out', 'w')

T = int(f_in.readline())

for t in xrange(1, T+1):
    N = list(f_in.readline()[:-1])

    p = -1
    for i in xrange(len(N) - 1):
        if int(N[i]) > int(N[i + 1]):
            p = i
            for j in xrange(i - 1, -1, -1):
                if int(N[j]) == int(N[p]):
                    p = j
                else:
                    break
            break

    if p != -1:
        N[p] = str(int(N[p]) - 1)
        for i in xrange(p + 1, len(N)):
            N[i] = "9"

    f_out.write("Case #" + str(t) + ": " + str(int("".join(N))) + "\n")
    #print "Case #" + str(t) + ":", int("".join(N))

f_in.close()
f_out.close()