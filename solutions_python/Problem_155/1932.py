import sys
with open(sys.argv[1]) as fh:
    T = int(fh.readline().strip())
    for i in range(T):
        M, S = fh.readline().strip().split(" ")
        curr_standing = 0
        n_friends = 0
        for j, c in enumerate(S):
            if curr_standing>=j:
                curr_standing+=int(c)
            else:
                n_friends+=(j-curr_standing)
                curr_standing+=int(c)+(j-curr_standing)
        print("Case #{0}: {1}".format(i+1, n_friends))
