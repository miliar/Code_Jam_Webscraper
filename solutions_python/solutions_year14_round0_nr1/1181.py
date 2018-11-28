def Magic():
    T = int(raw_input())
    for t in range(1, T + 1):
        ans1 = int(raw_input())
        grid1 = [raw_input().split() for _ in range(4)]
        ans2 = int(raw_input())
        grid2 = [raw_input().split() for _ in range(4)]
        num = set(grid1[ans1-1]) & set(grid2[ans2-1])
        _len = len(num)
        if _len == 1:
            print "Case #{}: {}".format(t, num.pop())
        elif _len == 0:
            print "Case #{}: Volunteer cheated!".format(t)
        else:
            print "Case #{}: Bad magician!".format(t)
Magic()
