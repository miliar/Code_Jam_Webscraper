

def run(n, k):
    nums = [n]
        
    for i in range(0, k):

        m = max(nums)
        new_m = 0
        if m % 2 == 0:
            new_m = m / 2
            nums[nums.index(m)] = new_m
            nums.append(new_m - 1)
            if i == k-1:
                return [new_m, new_m - 1]
        else:
            new_m = (m - 1) / 2
            nums[nums.index(m)] = new_m
            nums.append(new_m)
            if i == k-1:
                return [new_m, new_m]
        

t = int(raw_input())
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  rmax, rmin = run(n, k)
  print "Case #{}: {} {}".format(i, rmax, rmin)