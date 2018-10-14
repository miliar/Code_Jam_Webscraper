for case_num in xrange(input()):
    ans1 = input()
    grid1 = [map(int, raw_input().split()) for x in range(4)]
    ans2 = input()
    grid2 = [map(int, raw_input().split()) for x in range(4)]
    poss_ans = set()

    for num in grid1[ans1 - 1]:
        poss_ans.add(num)

    multiple_answers = 0
    final_ans = None
    for num in grid2[ans2 - 1]:
        if num in poss_ans:
            multiple_answers += 1
            final_ans = num

    if multiple_answers == 0:
        print 'Case #{0}: Volunteer cheated!'.format(case_num + 1)
    elif multiple_answers == 1:
        print 'Case #{0}: {1}'.format(case_num + 1, final_ans)
    else:
        print 'Case #{0}: Bad magician!'.format(case_num + 1)
