
with open('test1.txt','r') as file:
    
    t = file.readline()
    case = 1
    
    for line in file:
        row = line.split()
        
        standing = 0
        need = 0
        toInvite = 0
        
        for x in row[1]:
            x = int(x)       
            if standing >= need:
                 standing = standing + x
                 need = need + 1
            else:
                toInvite = toInvite + (need-standing)
                standing = standing + x + (need-standing)
                need = need + 1
                
        print 'Case #' + str(case) + ': ' + str(toInvite)
        case = case + 1