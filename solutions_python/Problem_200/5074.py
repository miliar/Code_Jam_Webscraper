ip = open('c:/py/input', 'r')
op = open('c:/py/output', 'w')
t = int(ip.readline())
i = 1
while i <= t:
    n = int(ip.readline())
    ns = str(n)
    ans = 0
    while n != 0:
        if n < 10:
            ans = n
            break
        else:
            na = []
            j = 0
            while j < len(ns):
                na.append(int(ns[j]))
                j += 1
            k = 0
            while k < (len(na)-1):
                if na[k] <= na[k+1]:
                    if k == (len(na)-2):
                        ans = n
                        break
                    k += 1
                else:
                    pc = n%pow(10,(len(na)-1))
                    if pc == 0:
                        n = n-((n%pow(10, (len(na)-1))+1))
                        ns = str(n)
                    else:
                        n -= 1
                        ns = str(n)
                    ans = 0
                    break
            if ans != 0:
                break
    op.write('Case '+'#'+str(i)+': '+str(ans)+'\n')
    print('Case '+'#'+str(i)+': '+str(ans)+'\n')
    i += 1
ip.close()
op.close()
                
