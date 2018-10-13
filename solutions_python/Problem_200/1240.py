from math import inf

t = int(input())

for i in range(1, t + 1):
    n = int(input())

    repeat = True
    while repeat:
        nums = []
        result = n
        tidy = True
        last = inf
        while n is not 0:
            r = n % 10

            if r > last:
                tidy = False
            nums.insert(0, r)
            last = r
            n //= 10

        if not tidy:
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j] -= 1
                    for z in range(j+1, len(nums)):
                        nums[z] = 9
                    break
        else:
            repeat = False

        n = int("".join([str(x) for x in nums]))

    print("Case #" + str(i) + ": " + str(n))