import sys
with open(sys.argv[1]) as fh:
    n = int(fh.readline())
    for case_no in range(1, n+1):
        max_shyness, shynesses = fh.readline().split(" ")
        min_friends = 0
        total_standing = int(shynesses[0])  # S0 stand up immediately
        max_shyness = int(max_shyness)
        shynesses = iter(int(i) for i in shynesses[1:].strip())

        for shyness, m in enumerate(shynesses, start=1):
            if total_standing <= shyness:
                need_to_invite = shyness - total_standing
                min_friends += need_to_invite
                total_standing += need_to_invite
            total_standing += m

        print("Case #{}: {}".format(case_no, min_friends))
