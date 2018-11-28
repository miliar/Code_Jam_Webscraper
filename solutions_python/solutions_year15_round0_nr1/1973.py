for T in xrange(int(raw_input())):
    S = map(int, raw_input().split(' ')[1])
    num_friends = 0
    num_standing = 0
    for s, n in enumerate(S):
        insert_friends = 0
        if num_standing < s:
            insert_friends = (s-num_standing)
            num_friends += insert_friends
        num_standing += insert_friends + n
    print "Case #{0}: {1}".format(T+1, num_friends)



