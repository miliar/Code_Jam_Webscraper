cases = input()

for i in xrange(cases):
    grid_old = []
    grid_new = []

    row_old = input() - 1
    for j in xrange(4):
        grid_old.append(set(raw_input().split(' ')))

    row_new = input() - 1
    for j in xrange(4):
        grid_new.append(set(raw_input().split(' ')))

    intersection = grid_old[row_old] & grid_new[row_new]
    if len(intersection) == 1:
        ans = list(intersection)[0]
    elif not intersection:
        ans = "Volunteer cheated!"
    else:
        ans = "Bad magician!"

    print 'Case #{num}: {ans}'.format(num=i+1,ans=ans)
