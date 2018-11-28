def last_tidy(n):
    nums = list(str(n))

    for i in range(len(nums)-1, 0, -1):
        if nums[i] < nums[i-1]:
            nums[i] = '9'
            for k in range(i+1,len(nums)):
                nums[k] = '9'
            nums[i-1] = chr(ord(nums[i-1]) - 1)
                
    return int(''.join(nums))
"""
print(last_tidy(132))
print(last_tidy(1000))
print(last_tidy(7))
print(last_tidy(111111111111111110))
print(last_tidy(101))
print(last_tidy(45748))
"""

with open('input.txt') as inf:
    with open('output.txt', 'w') as ouf:
        n = int(inf.readline().strip())
        for i in range(1, n+1):
            num = int(inf.readline().strip())
            ouf.write('Case #'+str(i)+': '+str(last_tidy(num))+'\n')
