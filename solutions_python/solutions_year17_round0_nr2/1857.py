t = int(raw_input().strip())
for i in range(t):
    num = map(int, raw_input().strip())
    for point in range(len(num) - 1):
        if num[point] <= num[point+1]:
            continue
        else:
            cutoff_point = point
            cutoff_num = num[point] - 1
            while cutoff_num < num[cutoff_point - 1]:
                if cutoff_point == 0:
                    break
                cutoff_point -= 1
                cutoff_num = num[cutoff_point] - 1

            num[cutoff_point] -= 1
            for j in range(cutoff_point+1, len(num)):
                num[j] = 9
    tidy_num = int(''.join(str(x) for x in num))
    print "Case #{0}: {1}".format(i+1, tidy_num)
