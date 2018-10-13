from sys import stdin

N = int(stdin.readline())

for case_idx in range(N):

    line = stdin.readline().strip().split(' ')
    M,S = float(line[0]), line[1]
 
    tsp = 0
    nr_friends = 0
    s_idx = 0

    for s in S:

        # current number of standing people
        sp = float(s)
        # total number of standing people
        tsp = tsp + sp

        # if there is more people
        if s_idx < M:
            
                # number of people of the next shyness level
                nsl = float(S[s_idx+1])
                #print('next shyness level:',nsl)
                #print('number of standing people',tsp)
                
                if (nsl > 0) and (tsp < (s_idx+1)):
                    nr_friends = int( nr_friends + int((s_idx+1) - tsp))
                    tsp = tsp + nr_friends

        # increase the shyness index
        s_idx = s_idx + 1

    print("Case #",str(case_idx+1),": ",str(nr_friends),sep="")

