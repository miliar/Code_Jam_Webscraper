


import sys



inputfile = open(sys.argv[1], 'r')
cases = int(inputfile.readline())

for i in range(cases):
    line = inputfile.readline()
    #print 'processing', line[:-1]
    nums = [int(n) for n in line.split()]
    numgoogs = nums[0]
    supplies = nums[1]
    p = nums[2]
    supplies_used = 0
    count = 0
    for n in nums[3:]:
        d = n - 3*p
        if n < p or p > 10:
            #print 'saying no because p: %s is bigger than n: %s'%(p, n)
            continue
        if d >= -2:
            #print 'counting n: %s because d:%s feels legit compared to p:%s'%(n,d,p)
            count += 1
        elif d >= -4 and supplies_used < supplies:
            count += 1
            supplies_used += 1
            #print 'counting n: %s because d:%s feels legit compared to p:%s and we"ve used %s of %s supplies'%(n,d,p, supplies_used, supplies)
        #else:
            #print 'not counting n: %s because d:%s is too wrong for p: %s... and maybe supplies (%s/%s)?'%(n,d,p, supplies_used, supplies)
    print "Case #%s: %s"%(i+1, count)        
    
