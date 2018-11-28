'''
Created on 12/04/2014

@author: tianyizhu
'''
from multiprocessing import Process, Manager

def f(ci, res, n1, n2, s1, s2):
    ans = []
    for n in s1[n1]:
        if n in s2[n2]:
            ans.append(n)
    if len(ans) == 0:
        res[ci] = "Volunteer cheated!"
    elif len(ans) > 1:
        res[ci] = "Bad magician!"        
    else:        
        res[ci] = ans[0]
    
if __name__ == "__main__":
    ps = []
    manager = Manager()
    fin = open("mt.in", "r")
    fout = open("mt.out", "w")
    t = int (fin.readline())
    res = manager.list(range(t))
    for ci in xrange(t):
        n1 = int (fin.readline()) - 1
        s1 = []
        for i in xrange(4):
            s1.append(fin.readline().strip().split(" "))
        n2 = int(fin.readline()) - 1
        s2 = []
        for i in xrange(4):
            s2.append(fin.readline().strip().split(" "))
        p = Process(target=f, args=(ci, res, n1, n2, s1, s2))
        ps.append(p)
        p.start()
    for ci in xrange(t):
        ps[ci].join()
        fout.write("Case #%d: %s\n" % (ci + 1, str(res[ci])))
    fout.close()
    fin.close()
