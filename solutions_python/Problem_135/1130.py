cases = int(input())
for case in range(cases):
    first_ans = int(input())
    first_arr = []
    for i in range(4):
        first_arr.append(set(map(int, input().split(' '))))
    sec_ans = int(input())
    sec_arr = []
    for i in range(4):
        sec_arr.append(set(map(int, input().split(' '))))

    s1 = first_arr[first_ans-1]
    s2 = sec_arr[sec_ans-1]
    i = list(s1.intersection(s2))
    if len(i) == 1:
        print("Case #{}: {}".format(case+1, i[0]))
    elif len(i) == 0:
        print("Case #{}: Volunteer cheated!".format(case+1))
    else:
        print("Case #{}: Bad magician!".format(case+1))

