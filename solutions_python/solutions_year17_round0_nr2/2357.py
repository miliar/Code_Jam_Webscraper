def findTidy(x):
    nums = [n for n in x]
    for i in range(len(nums)-1, 0, -1):
        ones = int(nums[i])
        tens = int(nums[i-1])
        if tens > ones:
            oneLess = int(''.join(nums[:i]))-1
            nums = [n for n in str(oneLess)] + ['9' for j in range(len(nums)-i)]
    return int(''.join(nums))







for x in range(eval(input())):
    print("Case #{}: {}".format(x+1, findTidy(input())))
