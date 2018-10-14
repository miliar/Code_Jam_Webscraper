import sys
ca = int(sys.stdin.readline())
for nu in range(ca):
    n,data = sys.stdin.readline().strip().split(' ')
    for ans in range(10010):
        sum = ans
        flag = 1
        for i in range(len(data)):
            if sum < i:
                flag = 0
                break
            else:
                sum += int(data[i])
        if flag:
            break
    print 'Case #%d: %d' %(nu+1,ans)

        
