INPUT = "C-small-1-attempt0.in.txt"
OUTPUT = "C-small-1-attempt0.out"

def BathroomStalls(N,K):
    dists = [N]
    i = 0
    while(i < K):
        maxDist = max(dists)
        LastmaxLR = maxDist / 2
        LastminLR = (maxDist - 1) / 2
        dists.append(LastmaxLR)
        dists.append(LastminLR)
        dists.remove(maxDist)
        i +=1

    return [LastmaxLR, LastminLR]
#
#
with open(INPUT) as infile:
    with open(OUTPUT, 'w') as outfile:
        numCases = int(infile.readline())

        for i in range(numCases):

            N, K = infile.readline().split()
            # print N
            # print K
            outfile.write("Case #%d: %d %d\n" % (i + 1, BathroomStalls(int(N),int(K))[0],BathroomStalls(int(N),int(K))[1]))
#


print BathroomStalls(1000,1000)
#
# print TidyNumbers("111111111111111110")
#
# strtest = 1111111111111111111111111111111123
# if (str(strtest) != "".join(sorted(str(strtest)))):
#     print ("yes working")
# # print "".join(sorted(str(strtest)))
