

tests = int(raw_input())

for t in xrange(tests):
    
    cache = {}
    tmp = map(int,raw_input().split())
    groups = map(int,raw_input().split())
    
    rounds = tmp[0]
    size = tmp[1]
    pointer = 0
    total = 0
    
    totalGroup = sum(groups)
    if(totalGroup<=size):
        print "Case #%d:"%(t+1),
        print totalGroup*rounds
        continue
    
    for i in range(rounds):
        if(pointer not in cache):
            joined = 0
            original = pointer
            while(joined+groups[pointer]<=size):
                if(pointer==original and joined>0):
                    break
                joined = joined + groups[pointer]
                pointer = pointer + 1
                if(pointer==len(groups)):
                    pointer = 0
            cache[original]=(pointer,joined)
            total = total + joined
        else:
            total = total + cache[pointer][1]
            pointer = cache[pointer][0]
            
    print "Case #%d:"%(t+1),
    print total