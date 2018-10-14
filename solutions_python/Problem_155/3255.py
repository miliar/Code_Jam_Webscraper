t = int(raw_input())

for i in xrange(t):
    task = raw_input().split()
    max_s = int(task[0])
    digits = [int(x) for x in task[1]]
    result = 0
    standing = digits[0]
    level = 1
    while level <= max_s:
        new_friends = 0
        if level > standing:
            new_friends = level - standing
        result += new_friends
        standing += new_friends + digits[level]
        level += 1
        
    
    
    
    
    print "Case #%d: %d" % (i+1, result)    
        
    