#f_in = open('A.in', 'r')
#f_in = open('A-small-attempt0.in', 'r')
f_in = open('A-large.in', 'r')
#f_out = open('A.out', 'w')
#f_out = open('A-small.out', 'w')
f_out = open('A-large.out', 'w')

T = int(f_in.readline())

for t in xrange(1, T+1):
    line_list = f_in.readline()[:-1].split(" ")
    S = list(line_list[0])
    K = int(line_list[1])

    flips = 0;
    for i in xrange(len(S) - K):
        if S[i] == "-":
            flips += 1
            for j in xrange(i, i + K):
                if S[j] == "-":
                    S[j] = "+"
                else:
                    S[j] = "-"

    C = 0
    for i in xrange(len(S) - K, len(S)):
        if S[i] == "-":
            C -= 1
        if S[i] == "+":
            C += 1

    f_out.write("Case #" + str(t) + ": ")
    #print "Case #" + str(t) + ":",
    if C == K:
        f_out.write(str(flips))
        #print flips
    elif C == -K:
        f_out.write(str(flips + 1))
        #print flips+1
    else:
        f_out.write("IMPOSSIBLE")
        #print "IMPOSSIBLE"
    f_out.write("\n")

f_in.close()
f_out.close()