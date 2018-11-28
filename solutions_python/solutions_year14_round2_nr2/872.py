def lottery(A,B,K):
    count = 0
    alist = [i for i in range(A) ]
    blist = [i for i in range(B) ]
    klist = [i for i in range(K) ]
    for a in alist:
        for b in blist:
            if a & b in klist:
                count = count+1
    return count
    


##Filename = 'A-small-practice.in'
Filename = 'B-small-attempt0.in'

with open(Filename,'r') as file_seq:
    line = file_seq.readline()
    numCases = int(line)
    for i in range(numCases):            
        line = file_seq.readline().split()
        A,B,K = int(line[0]),int(line[1]),int(line[2])
        flip = lottery(A,B,K)
        if flip == None:
            print 'Case #'+str(i+1)+': NOT POSSIBLE'
        else:
            print 'Case #'+str(i+1)+': '+str(flip)


