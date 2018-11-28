def solve(input):
    x = int(input.strip())
    nums = [int(_) for _ in input.strip()]
    for i in range(len(nums) - 1):
        if nums[-i - 1] > nums[-i - 2]:
            break
    else:
        nums.sort()
        #print nums
        #if nums[0] != 0:
        #ans = [nums[0]] + [0] + nums[1:]
        #else:
            #zeros = nums.count(0)
        """
            if zeros == len(nums) - 1:

            nums = [_ for _ in nums if _ != 0]
            ans = nums + [0] * (zeros + 1)

        """
        top = min([_ for _ in nums if _ != 0])
        nums.remove(top)
        ans = [top, 0] + nums




        return ''.join([str(_) for _ in ans])

    subs = nums[-i - 2:]
    top = 10
    j = 0
    for _j, _x in enumerate(subs):
        if _x > subs[0] and _x < top:
            top = _x
            j = _j
    del subs[j]
    subs.sort()
    ans = nums[:-i - 2] + [top] + subs
    return ''.join([str(_) for _ in ans])

if __name__ == '__main__':
    str_in = 'B-large.in'

    #str_in = 'B-small-attempt5.in'

    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            continue

        output = 'Case #' + str(i) + ': ' + solve(input)
        f_out.write(output + '\n')
        print output

    f_out.close()
