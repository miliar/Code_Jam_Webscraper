# read the input file
# fin = open('sample-A.in', 'r')
#fin = open('A-small-attempt0.in', 'r')
#fout = open('A-small.out', 'w')
fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

# get the number of test cases
T = int(fin.readline().rstrip('\n'))

# loop through the test cases
for t in range(T):

    # read this test case
    case_line = fin.readline().rstrip('\n')
    
    # get S max and S
    Smax, Sall = case_line.split(' ')
    Smax = int(Smax)
    
    # set the initial number of friends
    n_friends = 0    
    n_standing = 0

    # start with the first shyness level
    N0 = int(Sall[0])
    if N0 == 0:
        # if there are none, invite one friend
        n_friends += 1
        # update number standing
        n_standing += 1
    else:
        # update number standing
        n_standing += N0

    # loop through the remaining levels
    for S, N in enumerate(Sall[1:]):

        # convert N to integer
        N = int(N)        

        # adjust shyness level        
        S += 1

        # increase friends if needed
        while S > n_standing:
            n_friends += 1
            n_standing += 1
        
        # update number standing
        n_standing += N

    fout.write("Case #%d: %d\n" % (t+1, n_friends))

fin.close()
fout.close()
