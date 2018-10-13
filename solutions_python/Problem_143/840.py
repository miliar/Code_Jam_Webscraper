Klist = []
for case in range(int(raw_input())):
    count = 0
    A, B, K = map(int,raw_input().split())
    #print A, B, K

    for i in range(A):
        for j in range(B):
            x = i & j
            if x == 0 or 0 < x < K:
                count += 1
            #print i,j,x

    print "Case #"+str(case + 1) + ": " + str(count)

