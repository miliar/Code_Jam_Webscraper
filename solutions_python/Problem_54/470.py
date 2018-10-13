   
def gcd(big, small):
    if small > big:
        small, big = big, small
    if big % small == 0:
        return small
    else:
        return gcd(small, big-small);


f = open("small.in","r")
of = open("small.out","w")
flag = True
casenum = 0
for line in f:
    if(flag):
        T = int(line)
        flag = False
        continue
    casenum += 1

    line = line.strip()
    tmp = line.split(' ')
    N = int(tmp[0])
    nums = [int(s) for s in tmp[1:]]
    nums = list(set(nums))

    nowgcd = abs(nums[1] - nums[0])
    if ( nums[1] == nums[0] ):
        nowgcd = nums[1]
    
    for i in range(2,len(nums)):
        nowgcd = gcd(nowgcd, abs(nums[i]-nums[i-1]))

    if nums[0]%nowgcd == 0:
        of.write("Case #%d: %d\n" % (casenum,0))
    else:
        of.write("Case #%d: %d\n" % (casenum,nowgcd-(nums[0]%nowgcd)))

f.close()
of.close()
