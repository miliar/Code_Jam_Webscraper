#! /usr/bin/python

def magic(ans1, ans2, perm1, perm2):
    row1 = perm1[ans1 - 1]
    row2 = perm2[ans2 - 1]

    ans = []
    for c in row1:
        if c in row2:
            ans.append(c)
    return ans

fh = open("input")

count = int(fh.readline())

for i in range(count):
    ans1 = int(fh.readline())
    perm1 = []
    for j in range(4):
        perm1.append(fh.readline().split())
    ans2 = int(fh.readline())
    perm2 = []
    for j in range(4):
        perm2.append(fh.readline().split())
    ans = magic(ans1, ans2, perm1, perm2)

    print "Case #%d:" % (i + 1),
    if not ans:
        print "Volunteer cheated!"
    else:
        if len(ans) == 1:
            print ans[0]
        else:
            print "Bad magician!"

