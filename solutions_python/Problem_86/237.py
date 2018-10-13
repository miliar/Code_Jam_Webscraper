def ishar(x,y):
    if(x%y == 0 or y%x == 0):
        return True
    return False

case = int(raw_input())
for tt in range(1,case+1):
    x = raw_input().split()
    other = raw_input().split()
    for i in range(len(other)):
        other[i] = int(other[i])
    for ans in range(int(x[1]),int(x[2])+1):
        can = True
        for i in other:
            if(not ishar(i,ans)):
                can = False
                break
        if(can):
            print 'Case #' + str(tt) + ': ' + str(ans)
            break
    if(not can):
        print 'Case #' + str(tt) + ': NO'
