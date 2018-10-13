lines = [x for x in open('A-large.in', 'rt').readlines()][1:]
results = []
for line in lines:
    nums = line.split()[1]
    first_num = nums[0]
    nums = nums[1:]
    
    count = int(first_num)
    res = 0
    for ind, num in enumerate(nums):
        if num == '0':
            continue
        if ind + 1 > count:
            res += ind + 1 - count
            count += ind + 1 - count

        count += int(num)
    results.append(res)
        
# Print results
outfile = open('A-large.out', 'wt')
for ind, res in enumerate(results):
    print 'Case #%d: %s' % (ind + 1, res)
    outfile.write('Case #%d: %s\n' % (ind + 1, res))
outfile.close()