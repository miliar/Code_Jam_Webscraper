def snapper(i, n , k):
    var = []
    result = []
    
    while n >0 :
        var.append('0')
        result.append('1')
        n -= 1
    #print var
    #print result

    while k>0:
        x = len(var)-1
        try:
            x = var.index('0')
        except :
            pass
        #print k,x
        while x >=0:
            #print '-',var[x]
            if var[x] == '0':
                #print 't'
                var[x] = '1'
            else :
                #print 'f'
                var[x] = '0'
            #print '=',var[x]
            x -= 1
        k -= 1
    out = 'Case #'+str(i)+': '+('ON'if var == result else 'OFF')
    print out

def main():
    with open('A-small.in') as inputFile:
        cases = int(inputFile.next())
        i = 1
        for l in inputFile:
            ls = l.strip().split(' ')
            snapper(i,int(ls[0]),int(ls[1]))
            i += 1
        

main()
#snapper(1,4,47)

