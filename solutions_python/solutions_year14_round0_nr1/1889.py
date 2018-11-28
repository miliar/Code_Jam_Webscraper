#!/usr/bin/env python

problem = 'A-small-attempt1'

fin = open(problem + '.in')
fout = open(problem + '.out', 'w')

def read_ints():
    return {int(x) for x in fin.readline().strip().split()}

T = int(fin.readline())

for caseno in range(T):
    ans1 = int(fin.readline())
    grid1 = [read_ints() for _ in range(4)]
    row1 = grid1[ans1-1]
    ans2 = int(fin.readline())
    grid2 = [read_ints() for _ in range(4)]
    row2 = grid2[ans2-1]
    nums = row2.intersection(row1)

    if len(nums) == 0:
        result =  'Volunteer cheated!'
    elif len(nums) > 1:
        result = 'Bad magician!'
    else:
        result = nums.pop()

    fout.write("Case #%d: %s\n" % (caseno+1, result))

fout.close()
