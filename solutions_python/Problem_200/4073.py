def p(n, l):
    #print n, l
    if l == 1:
        return n
    if n[0] == '0':
        return '9'*(len(n)-1)
    else:
        return str(int(n[0])-1) + '9'*(len(n)-1)

    
def pp(n):
    n = str(n)
    l = len(n)
    if l == 1:
        return n
    i = 0
    while i < l-2 and int(n[i]) <= int(n[i+1]):
        i+=1
    #print "i",i
    if i == l-2 and int(n[i]) <= int(n[i+1]):
        return n
    else:
        trail = p(n[i:], l-i+1)
        #print "recieved trail", trail
        while i>0 and int(n[i-1]) > int(trail[0]):
            i-=1
            trail = p(n[i:], l-i+1)
            #print "ongoing trail", trail
        #print "final trail", trail
        return int(n[:i] + trail)


t = input()
for i in range(1, t + 1):
    n = input()
    print "Case #{}: {}".format(i, pp(n))
