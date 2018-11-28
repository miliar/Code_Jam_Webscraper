def GCD(x, y):
    if x < 0 : x = -x
    if y < 0 : y = -y

    if x + y > 0 :
        g = y
        while x > 0:
            g = x
            x = y % x
            y = g
        return g
    else:
        return 0
  
def solve(f, t, nums):
        nod = nums[1] - nums[2]
        for i in range(3, len(nums)):
                nod = GCD(nod, nums[1] - nums[i])

        if nod < 0 : nod = -nod
        
        y = 0
        if (nums[1] % nod) != 0:
                y = nod - (nums[1] % nod)
        f.write("Case #{0}: {1}\n".format(t, y))

fp = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
#fp = open('B-small-attempt0.in', 'r')
#fo = open('B-small-attempt0.out', 'w')

tt = int(fp.readline())
for t in range(1, tt + 1):
        s = fp.readline().split(' ')
        nums = []
        for x in s:
                nums.append(int(x))
        solve(fo, t, nums)

fp.close()
fo.close()
