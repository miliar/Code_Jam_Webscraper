

def main():
    grid1 = list()
    grid2 = list()
    with open("input", "r") as myInput:
        n = int(myInput.readline())
        for a in xrange(n):
            b = int(myInput.readline())
            grid1.append(myInput.readline().strip('\n').split(' '))
            grid1.append(myInput.readline().strip('\n').split(' '))
            grid1.append(myInput.readline().strip('\n').split(' '))
            grid1.append(myInput.readline().strip('\n').split(' '))
            c = int(myInput.readline())
            grid2.append(myInput.readline().strip('\n').split(' '))
            grid2.append(myInput.readline().strip('\n').split(' '))
            grid2.append(myInput.readline().strip('\n').split(' '))
            grid2.append(myInput.readline().strip('\n').split(' '))
            checkRow(b-1,c-1, a+1, grid1, grid2)
            grid1 = grid1[0:0]
            grid2 = grid1[0:0]


def checkRow(n0, n1, d, grid1, grid2):
    l1 = grid1[n0]
    l2 = grid2[n1]
    se = set()
    for a in l1:
        for b in xrange(4):
            if a == l2[b]:
                se.add(a)
    with open("output", "a") as myOutput:
        if len(se) > 1:
            myOutput.write("Case #{}: Bad magician!\n".format(d))
        elif len(se) == 0:
            myOutput.write("Case #{}: Volunteer cheated!\n".format(d))
        else:
            k = se.pop()
            myOutput.write("Case #{}: {}\n".format(d, k))
    

main()