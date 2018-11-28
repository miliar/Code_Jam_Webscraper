input = "A-large.in"

with open(input, "r") as input_file:
    nb_case = int(input_file.readline())
    for count in xrange(nb_case):
        nb = int(input_file.readline())
        S1 = 0
        S2 = 0
        M = 0
        plates = [int(x) for x in input_file.readline().split()]
        for i in xrange(nb-1):
            S1 += max(0, plates[i] - plates[i+1])
            M = max(M, plates[i] - plates[i+1])
        for i in xrange(nb-1):
            S2 += min(M, plates[i])
        print "Case #%d:" %(count+1), S1, S2
