def isrecycled(n,nums):
    tmp = n
    tmp = tmp[-1]+tmp[:-1]
    ret = []
    while tmp != n:
        if tmp in nums:
            ret.append(tmp)
        tmp = tmp[-1]+tmp[:-1]

    return ret

def answer(s):
    A, B = [int(x) for x in s.split(' ')]

    nums = [str(x) for x in range(A,B+1)]
    count = 0

    for i in nums:
        r = isrecycled(i,nums[nums.index(i):])
        count += len(r)

    return count
    


f = open('C-small-0.in','r')

n = int(f.readline())

out_s = ''
for case in range(n):
    out_s += 'Case #'+str(case+1)+': '
    
    out_s += str(answer(f.readline().strip()))

    out_s += '\n'

#print out_s
f = open('C-small-0.out','w')
f.write(out_s)
