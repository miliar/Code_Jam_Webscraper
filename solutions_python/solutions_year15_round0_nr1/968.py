import numpy as np
    

def ovation(filepath):
    
    with open('../data/output1.txt', 'w') as g:
        with open(filepath) as f:
            
            N = int(f.readline())
            
            for i in range(N):
                n, k = f.readline().split(' ')
                n, k = int(n), k
                
                k = np.array([int(x) for x in list(k[:-1])])    
                c = np.cumsum(k) - np.array(range(n + 1))
                c[n] = n + 1
                m = 1 - np.min(c)
                m = max(0, m)
                
                g.write("Case #%s: %s\n" % (i + 1, m))
                print "Case #%s: %s" % (i + 1, m)
        
if __name__=="__main__":
    
#     ovation("../data/shytest.txt")
    ovation("../data/A-small-attempt0.in.txt")
        
    