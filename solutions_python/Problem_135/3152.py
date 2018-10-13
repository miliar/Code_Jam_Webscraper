def main():
    test_cases = int(raw_input())
    for test_case in range(test_cases):
        poss_comb = [set(), set()]

        for att in range(2):
            # Read the volunteer's guess
            guess = int(raw_input())
            # Read the grid
            grid = []
            for i in range(4):
                grid.append( map(int, raw_input().split()) )
            poss_comb[att] = set(grid[guess-1])

        poss_ans = poss_comb[0].intersection(poss_comb[1])
        if len(poss_ans) == 0:
            print 'Case #%d: Volunteer cheated!' % (test_case+1)
        elif len(poss_ans) == 1:
            print 'Case #%d: %d' % (test_case+1, list(poss_ans)[0])
        else:
            print 'Case #%d: Bad magician!' % (test_case+1)


if __name__ == '__main__':
    main()
