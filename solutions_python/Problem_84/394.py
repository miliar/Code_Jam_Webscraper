def algo(C, R, m):
    cs = 0
    for i in xrange(0,R):
        for j in xrange(0,C):
          if m[i][j] == "#": cs += 1

    if cs % 4 == 0:
        for i in xrange(0,R):
            for j in xrange(0,C):
                try:
                    if m[i][j] == "#":

                        m[i][j] = '/'
                        m[i][j+1] = "\\"

                        m[i+1][j] = "\\"
                        m[i+1][j+1] = "/"
                        
                except IndexError:
                    return "Impossible"
        ms = ["".join(m[i]) for i in xrange(R)]
        return "\n".join(ms)

    else: return "Impossible"

f = open("a.in", "r")
content = f.readlines()

T =  int(content[0])
#print "T is {0}".format(T)

i = 1
case = 1
while i < len(content):
    c = content[i].rstrip("\n").split(" ")

    R = int(c[0])
    C = int(c[1])

    matr = [[] for j in xrange(R)]

    for j in xrange(i+1, i + R+1):
        matr[j-i-1] = list(content[j].rstrip("\n"))

    #print matr
    i += R+1


    print ("Case #{0}:\n{1}".format(case, algo(C,R,matr)))
    case += 1