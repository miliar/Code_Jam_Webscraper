input = "D-small-attempt2.in"

with open(input, "r") as input_file:
    nb_case = int(input_file.readline())

    for count in xrange(nb_case):
        X, R, C = [int(i) for i in input_file.readline().split()]
        m = min(R, C)
        M = max(R, C)
        if X == 4 and m == 2 and M == 4:
            print "Case #%d:" %(count+1), "RICHARD"
        elif X >= min(M + 1, 2*m + 1):
            print "Case #%d:" %(count+1), "RICHARD"
        elif R*C % X != 0:
            print "Case #%d:" %(count+1), "RICHARD"
        else:
            print "Case #%d:" %(count+1), "GABRIEL"
