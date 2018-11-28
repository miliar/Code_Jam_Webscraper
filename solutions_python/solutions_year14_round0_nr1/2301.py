times = int(input())

for i in range(1, times+1):
    row = int(input())
    for j in range(row-1):
        input()
    l = input().split()
    for j in range(4-row):
        input()
    row = int(input())
    for j in range(row-1):
        input()
    l2 = input().split()
    for j in range(4-row):
        input()
    ans = []
    for e in l:
        if e in l2:
            ans.append(e)
    if len(ans) == 0:
        r = 'Volunteer cheated!'
    elif len(ans) == 1:
        r = ans[0]
    else:
        r = 'Bad magician!'
    print("Case #%d: %s" % (i, r))
