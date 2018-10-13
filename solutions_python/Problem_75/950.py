n = int(raw_input())

for x in range(n):
    line = raw_input().split()

    ans = []
    #combine charactor dictionary
    combine = {}
    #oppose charactor list
    oppose = []
    
    m = int(line[0])
    line = line[1:]
    for y in range(m):
        tmp = line[0]
        line = line[1:]
        combine[tmp[0:2]] = tmp[2]
    #print "combine ", combine
        
    m = int(line[0])
    line = line[1:]
    for y in range(m):
        tmp = line[0]
        line = line[1:]
        oppose.append((tmp[0], tmp[1]))
    #print "oppose  ", oppose

    for y in line[1]:
        ans.append(y)
        
    #print ans
    y = 0
    while y < len(ans)-1:
        tmp = ans[y] + ans[y+1]
        #print y
        #print tmp
        if tmp in combine:
            ans[y:y+2] = combine[tmp]
            y -= 1
        else:
            tmp = ans[y+1] + ans[y]
            #print tmp
            if tmp in combine:
                ans[y:y+2] = combine[tmp]
                y -= 1
                
        for i, j in oppose:
            if i in ans[:y+2] and j in ans[:y+2]:
                a = ans.index(i)
                b = ans.index(j)
                if a >= 0 and b >= 0 and a != b:
                    ans[:y+2] = []
                    y = -1
        y += 1
        #print ans
    
    
    if len(ans) > 1:
        print "Case #%d: [%c," %(x+1, ans[0]),
        for y in ans[1:len(ans)-1]:
            print "%c," %y,
        if len(ans) > 0:
            print "%c]" %(ans[len(ans)-1])
    elif len(ans) == 1:
        print "Case #%d: [%c]" %(x+1, ans[0])
    else:
        print "Case #%d: []" %(x+1)
    
