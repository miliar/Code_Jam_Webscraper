'''
Created on Apr 8, 2017

@author: davidkogosov
'''
import unittest
count = 1


class Stall:
    def __init__(self, ls, rs, num):
        self.ls = ls
        self.rs = rs
        self.num = num
        self.occup = False
    

def process(filename):
    f = open(filename)
    num = int(f.readline())
    #print 'num', num
    for i in range(num):
        l = f.readline()
        elms = l.split()
        solve(int(elms[0]), int(elms[1]))
    f.close()

def solve(n, k):
    global count 
    out = 'Case #' + str(count) + ":"
    tmp = sol(n, k)
    print out, tmp[0], tmp[1]
    count += 1    

def sol(n, k):
    stalls = []
    ls = 0
    rs = n - 1
    num = 0
    for i in range(n):
        stalls.append(Stall(ls, rs, num))
        ls += 1
        rs -= 1
        num += 1
        
    #printstalls(stalls)
    index = 0
    for i in range(k):
        index = update_stalls(stalls, i==k-1)
        
    ls = stalls[index].ls
    rs = stalls[index].rs
    max_ = max(ls, rs)
    min_ = min(ls, rs)
    #print "chose", index
    #print "maxmin", max_, min_
    
            
        
    return (max_, min_)
 
def printstalls(stalls): 
    for stall in stalls:
        print stall.num, stall.ls, stall.rs
         
def calcls(stalls):
#     ls = []
#     index = 0
#     ls[index] = 0
#     for elm in stalls:
#         if stalls
     pass
 
 
def choose_stall(stalls):
    chosenindexes = []
    minlsrs = -1
    
    for idx, stall in enumerate(stalls):
        if stall.occup == True:
            continue
        
        ls = stall.ls
        rs = stall.rs
        min_ = min(ls, rs)
        if min_ > minlsrs:
            minlsrs = min_
            chosenindexes = []
            chosenindexes.append(idx)
        elif min_ == minlsrs:
            chosenindexes.append(idx)
            
    #print chosenindexes
            
    if len(chosenindexes) == 1:
        return chosenindexes[0]
    
    chosenindexes2 = []
    maxlsrs = 0
    for idx in chosenindexes:
        ls = stalls[idx].ls
        rs = stalls[idx].rs
        max_ = max(ls, rs)
        if max_ > maxlsrs:
            chosenindexes2 = []
            chosenindexes2.append(idx)
            maxlsrs = max_
        elif max_ ==maxlsrs:
            chosenindexes2.append(idx)
            
    return chosenindexes2[0]
            
        
        
 
def update_stalls(stalls, last):
    index = choose_stall(stalls)
    stalls[index].occup = True
    
    #print "before update"
    #printstalls(stalls)
    if not last:
        for idx in range(index+1, len(stalls)):
            ls = stalls[idx].ls
            delta = idx - index - 1
            
            if ls > delta:
                stalls[idx].ls = delta
        
        for idx in range(0, index):
            rs = stalls[idx].rs
            delta = index - idx - 1
            
            if rs > delta:
                stalls[idx].rs = delta
    
    #print "chose ", index
    #printstalls(stalls)
    return index
    

 
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        #process('/Users/davidkogosov/Downloads/bath1.txt')
        process('/Users/davidkogosov/Downloads/C-small-1-attempt0.in')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()