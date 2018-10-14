'''
Created on 2014-5-3

@author: ezonghu
'''
def solve(A,B,K):
    Ks = range(K)
    As = range(A)
    Bs = range(B)
    
    res = 0
    for a in As:
        for b in Bs:
            if (a & b) in Ks:
                res += 1
                
    return res
        
       
def process():
    fn="C:/Users/ezonghu/Downloads/B-small-attempt0"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    Cases = int(fi.next())
    CaseId = 0
     
    for l in fi:
        [A,B,K] = [int(i) for i in l.split()]
        res = solve(A,B,K)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res)
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()
    
process()