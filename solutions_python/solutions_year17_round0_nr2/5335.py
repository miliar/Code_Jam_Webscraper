test_cases = int(input())
last_tidy_num = 1

for i in range(0, test_cases):
    num  = int(input())
    for j in range(1, num+1):
        nums = list(map(int, str(j)))
        is_tidy = True

        for k in range(0, len(nums)-1):
            current_num = nums[k]
            next_num = nums[k+1]
            if current_num > next_num:
                is_tidy = False
                break

        if is_tidy == True:
            last_tidy_num = j

    print("Case #%d: %d" % (i+1, last_tidy_num))
