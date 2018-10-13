

def check(mylist, row, col):
    for x in xrange(row):
        for y in xrange(col):
            #can u find an path to the edge
            nocnt = 0
            #right->left
            i = 0
            while(i<col):
                if(mylist[x][y]<mylist[x][i]):
                    nocnt += 1
                    break
                i += 1
            #down->up
            i = 0
            while(i<row):
                if(mylist[x][y]<mylist[i][y]):
                    nocnt += 1
                    break
                i += 1

            if nocnt==2:
                return "NO"

    return "YES"



inp = open("B-small-attempt3.in", "r")
T = int(inp.readline())
for t in xrange(T):
    tmp = inp.readline().replace("\n", "").split(" ")
    N = int(tmp[0])
    M = int(tmp[1])
    mylist = list()
    for i in xrange(N):
        mylist.append(inp.readline().replace("\n", "").split(" "))

    #for row in mylist:
    #    print row
    print "Case #"+ str(t+1) + ": " + check(mylist, N, M)


