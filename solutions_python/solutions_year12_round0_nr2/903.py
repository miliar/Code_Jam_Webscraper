
f = open("blargeinput.txt")

a = 0

for line in f:
    if a == 0:
        a += 1
        continue
    yes = 0
    no = 0
    maybe = 0
    nums = line.split(" ")
    del(nums[0])
    surprises = int(nums[0])
    thresh = int(nums[1])
    del(nums[0])
    del(nums[0])
    for n in nums:
        score = int(n)
        sub1 = score/3.
        if (sub1 % 1) == 0:
            sub2 = sub1
            sub3 = sub1
            best = sub1 + 1
        else:
            sub1 = int(sub1)
            sub2 = (score-sub1)/2.
            if (sub2 % 1) == 0:
                sub3 = sub2
                best = sub2 + 1
            else:
                sub2 = int(sub2)
                sub3 = score - (sub1 + sub2)
                best = max([sub1,sub2,sub3])
        m = [sub1,sub2,sub3]
        m = max(m)
        if m == 0:
            best = 0
        if m >= thresh:
            yes += 1
            continue
        elif best >= thresh:
            maybe += 1
            continue
        else:
            no += 1
            continue
    winners = yes
    if maybe < surprises:
        winners += maybe
    elif maybe >= surprises:
        winners += surprises
    print "Case #" + str(a) + ": " + str(winners)
    a += 1
            
                
