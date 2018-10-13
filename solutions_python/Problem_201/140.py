filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round Qualification\\C\\C-large"


fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

def split(left, right):
    center = (left + right)/2
    return center, center-left-1, right-center-1
    

for T in xrange(trials):
        n, k = map(int, fin.readline().split(' '))
        
        left, right = 0, n+1
        kbin = ""
        while k > 0:
            center, ls, rs = split(left, right)
            #print center, left, right
            kbin += str(k%2)
            
            if (k % 2 == int(ls < rs)):
                right = center
            else:
                left = center
            
            k /= 2
        
        #print kbin
        
        fout.write("Case #{0}: {1} {2}\n".format(T+1, max(ls, rs), min(ls, rs)))
                    
fin.close()
fout.close()