#f = open("inputq1.txt", "r")
#f = open("A-small-attempt0.in","r")
f = open("A-large.in","r")
T = int(f.readline().split("\n")[0])

# for each test case
for i in range(0, int(T)):

    # read in the values
    data = f.readline().split("\n")[0].split(" ")
    ms = int(data[0])
    sls = str(data[1])

    # base case
    if( ms == 0 ):
        ans = 0

    else:
        num_p = sls[0]
        invite = 0
        for j in range(1, ms+1):
            if( int(num_p) >= int(j) ):
                num_p = int(num_p) + int(sls[j])

            else:
                invite = invite + int( int(j) - int(num_p) )
                num_p = int(num_p) + int( int(j) - int(num_p) ) + int(sls[j])

        ans = int(invite)


    print "Case #" + str(i+1) + ": " + str(ans)
