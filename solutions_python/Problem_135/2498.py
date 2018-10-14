def solve():
    guess_1=int(raw_input())
    table_1 = [map(int, raw_input().split()) for i in range(4)]

    guess_2=int(raw_input())
    table_2 = [map(int, raw_input().split()) for i in range(4)]

    line_1 = table_1[guess_1-1]
    line_2 = table_2[guess_2-1]

    inter=list(set(line_1) & set(line_2))

    if len(inter) == 0:
        ans = 'Volunteer cheated!'
    elif len(inter) == 1:
        ans = str(inter[0])
    else:
        ans = 'Bad magician!'
    return ans


for i in range(int(raw_input().strip())):
    ans = solve()
    print "Case #%d: %s" % (i+1, ans)
