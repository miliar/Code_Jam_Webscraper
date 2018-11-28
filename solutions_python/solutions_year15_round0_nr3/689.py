import numpy as np

#                  1  |  i  |  j  |  k   
quat = np.array([['+1', '+i', '+j', '+k'],  # 1
                 ['+i', '-1', '+k', '-j'],  # i
                 ['+j', '-k', '-1', '+i'],  # j
                 ['+k', '+j', '-i', '-1']]) # k

idx = {'1': 0, 'i': 1, 'j': 2, 'k': 3}

def mul(a, b):
    sgn = a[0]
    q = quat[idx[a[1]], idx[b]]
    if sgn != q[0]:
        return '-%s' % q[1] 
    else:
        return '+%s' % q[1]

def ass(l):
    s = '+1'
    l2 = []
    for e in l:
        s = mul(s, e)
        l2.append(s)
    return np.array(l2)

def is_ijk(l):
    if len(l) < 3:
        return "NO"
    
    li = ass(l)
    li, nd = li[:-2], li[-1]
    if nd != '-1':
        return "NO"
    idxi = np.where(li == '+i')[0]
    for i in idxi:
        lj = ass(l[i+1:])
        lj, nd = lj[:-1], lj[-1]
        if nd != '+i':
            return "NO"
        idxj = np.where(lj == '+j')[0]
        for j in idxj:
            if ass(l[i+j+2:])[-1] == '+k':
                return "YES"
    return "NO"

def main(filename):
       
    with open('../data/output3.txt', 'w') as g: 
        with open(filename) as f:
            
            N = int(f.readline())
            
            for i in range(N):
                L, X = f.readline().split()
                l = list(f.readline()[:-1]) * int(X)
                g.write("Case #%s: %s\n" % (i + 1, is_ijk(l)))
                print "Case #%s: %s" % (i + 1, is_ijk(l))
            

if __name__=="__main__":
    main("../data/plop.txt")
#     main("../data/dijkstratest.txt")