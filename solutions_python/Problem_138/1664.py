def data(filename):
    fi = open(filename,'r')
    o = open(filename+".out",'w')
    tests = fi.readline().strip()
    a = fi.readlines()
    for i in range(0,int(tests)):
        naomi = sorted(map(float,a[3*i+1].strip().split()))
        ken = sorted(map(float,a[3*i+2].strip().split()))
        while naomi and not beats(naomi,ken):
            naomi.remove(min(naomi))
            ken.remove(max(ken))
        dec = 0
        if naomi:
            dec = len(naomi)
        naomi = sorted(map(float,a[3*i+1].strip().split()))
        ken = sorted(map(float,a[3*i+2].strip().split()))
        hon = 0
        while naomi:
            m = max(naomi)
            naomi.remove(max(naomi))
            if m > max(ken):
                hon += 1
                ken.remove(min(ken))
            else:
                j = 0
                while j< len(ken)-1 and ken[j] < m:
                    j+=1
                ken.remove(ken[j])
        o.write("Case #" + str(i+1) + ": %d %d\n" % (dec,hon))
    fi.close()
    o.close()
    
def beats(n,k):
    for i in xrange(0,len(n)):
        if n[i] < k[i]:
            return False
    return True