import itertools

T = input()
for case_num in range(1, T + 1):
    _, levels = raw_input().strip().split(" ")
    levels = [int(c) for c in levels]

    num_extras = 0
    num_standing = 0

    for i, num_people in enumerate(levels):
        if num_standing < i:
            needed = i - num_standing
            num_extras += needed
            num_standing += needed

        num_standing += num_people

    print "Case #%d: %s" % (case_num, num_extras)
