


##def is_legal (lst, D):
##    for i in range(len(lst)-1):
##        if lst[i][1] > lst[i+1][0]-D:
##            return False
##    return True


def fix_problem (lst, D):
    for i in range(len(lst)-1):
        if lst[i][1] > lst[i+1][0]-D:
            leftmost = lst[i][0]
            rightmost = lst[i+1][1]
            max_time = max(lst[i][2],lst[i+1][2])
            if lst[i][2] > lst[i+1][2]:
                rng = lst[i+1][1]-lst[i+1][0]
                time_diff = lst[i][2] - lst[i+1][2]
                rightmost = min(lst[i+1][1]-lst[i+1][0]+lst[i][1]+D,  lst[i+1][1]+time_diff)               
                lst[i+1] = rightmost-rng, rightmost, lst[i][2]
            elif lst[i][2] < lst[i+1][2]:
                rng = lst[i][1]-lst[i][0]
                time_diff = lst[i+1][2] - lst[i][2]
                leftmost = max( lst[i+1][0]-D-(lst[i][1]-lst[i][0]), lst[i][0]-time_diff)
                lst[i] = leftmost, leftmost+rng, lst[i+1][2]
            if lst[i][1] > lst[i+1][0]-D:
                x = (lst[i][1]+D-lst[i+1][0])/2
                lst[i] = (lst[i][0]-x, lst[i+1][1]+x, lst[i][2]+x)
                del lst[i+1]
            return True
    return False

fin = open ('c:/users/hai/my projects/google code jam/2011/1B/B/B-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/1B/B/B-large.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    C,D = map(int, fin.readline().split())
    print(C,D)
    l = []
    for i in range(C):
        P,V = map(int,fin.readline().split())
        l.append((P,V))
    l.sort()
    l2 =[]
    for i in range(len(l)):
        P,V = l[i]
        l2.append((P-(V-1)*D/2, P+(V-1)*D/2, (V-1)*D/2))

    #print(l2)
    while fix_problem(l2,D):
        #print(l2)
        pass
    #print(l2)
  
    t = max([x[2] for x in l2])

    otpt = 'Case #'+str(testcase) +': ' + str(t)
    print(otpt)
    #print()
    #print()
    #print()
    fout.write(otpt+'\n')
    
    
        

fin.close()
fout.close()
