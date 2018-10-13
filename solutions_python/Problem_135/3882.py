def read_tests():
    with open('soln','w') as soln:
        with open('p1data') as f:
            ntests = int(f.readline())
            #print ntests

            for rnd in range(ntests):
                answer1,grid1 = read_test(f)
                answer2,grid2 = read_test(f)
                #print rnd,answer1,answer2
                p1(answer1,answer2,grid1,grid2,rnd+1,soln)

def read_test(f):
    answer = int(f.readline())
    grid = [[int(x) for x in f.readline().split()]
            for s in range(4)]
    return answer,grid

def p1(x,y,grid1,grid2,rnd,soln):
    rightnum = []
    for n in range(1,17):
        if n in grid1[x-1] and n in grid2[y-1]:
            rightnum.append(n)

    #print rightnum
    if len(rightnum) == 0:
        print >>soln, "Case #%i: Volunteer cheated!" % rnd
    elif len(rightnum) == 1:
        print >>soln, "Case #%i: %i" % (rnd,rightnum[0])
    elif len(rightnum) > 1:
        print >>soln, "Case #%i: Bad magician!" % (rnd)

if __name__ == "__main__":
    read_tests()
