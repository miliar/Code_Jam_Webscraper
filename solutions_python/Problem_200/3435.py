INPUT = "B-large.in.txt"
OUTPUT = "B-large.out"

def TidyNumbers(N):
    length =len(N)

    for j in range(length):
        for i in range(length):
            if ( i +1< length):
                if int(N[i]) > int(N[i+1]):
                    if N[i] == '1' and N[i + 1] == '0':
                        N = N[:i] + '0' + N[i + 1:]
                    else:
                        N = N[:i] + str(int(N[i])-1) + N[i + 1:]
                    N = N[:i+1] + '9'*(length-(i+1))
                    # print N


                            # N = N[:length-j]

    return N.lstrip('0')
    #

    # for i in range(N):
    #     if (str(N-i) == "".join(sorted(str(N-i)))):
    #         return N-i
    # if (N != "".join(sorted(N))):
    #     N = int(N) - 1
    #     return TidyNumbers(str(N))
    # return N

#
with open(INPUT) as infile:
    with open(OUTPUT, 'w') as outfile:
        numCases = int(infile.readline())

        for i in range(numCases):

            N = infile.readline().strip()
            # print N
            # print K
            outfile.write("Case #%d: %s\n" % (i + 1, TidyNumbers(N)))
#


print TidyNumbers("111111111111111110")
#
# strtest = 1111111111111111111111111111111123
# if (str(strtest) != "".join(sorted(str(strtest)))):
#     print ("yes working")
# # print "".join(sorted(str(strtest)))
