inf = open('C-small-attempt1.in', 'r')
outf = open('C-small-attempt1.out', 'w')

T = int(inf.readline())
for case in range(1, T+1):
    (N,L,H) = inf.readline().rstrip().split(' ')
    P = inf.readline().rstrip().split(' ')
    p=-1
    for i in range(int(L),int(H)+1):
        y=True
        for p2 in P:
            if int(p2)%i != 0 and i%int(p2) != 0:
                y=False
                break
        if y:
            p=i
            break
    if p == -1:
        p="NO"
    print p
    outf.write('Case #' + str(case) + ': ' + str(p) + '\n')
  #  print 'Case #' + str(case) + ': '

outf.close()
inf.close()
