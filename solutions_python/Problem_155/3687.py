
def getInviter(n, arr):
    sum = 0
    gap = 0
    for x in range(0, n+1):
        v = int(arr[x])
        if v > 0 :
            if sum < x :
               gap += (x - sum)
               sum += gap

            sum += int(arr[x])
#        print 'x: %d | sum: %d | gap: %d' % (x, sum, gap)
    return gap
    



# getInviter(4, "11111")                
# getInviter(1, "09")
# getInviter(5, "110011")
# getInviter(0, "1")
# getInviter(6, "1009001")
# getInviter(6, "9001001")
# getInviter(6, "1001009")

def execute(file):
    with open(file + '.output', 'w+') as o:
        with open(file) as f:
            content = f.read().splitlines()
            num = int(content[0])
            for i in range(1, num+1):
                (n, arr) = content[i].split(' ')
                o.write('Case #%d: %d\n' % ( i,getInviter(int(n), arr)))


execute('A-small-attempt0.in')
    
