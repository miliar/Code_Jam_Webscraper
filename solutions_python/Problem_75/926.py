'''
Created on May 7, 2011

@author: mario
'''
import sys

class MagickaSolver(object):
    
    def __init__(self, C, D):
        self.queue = []
        self.combine = C
        self.destroy = D
    
    def do_invoke(self, el):
        #print "Invoked", el,
        self.queue.append(el)
    
    def do_combine(self):
        if len(self.queue) < 2:
            return
        active_els = self.queue[-2] + self.queue[-1]
        #print "Combining ", active_els, 
        if active_els in self.combine:
            self.queue.pop()
            self.queue.pop()
            self.queue.append(self.combine[active_els])
            #print " = ", self.queue[-1],
        #else:
            #print "...nothing happens", 
    
    def do_oppose(self):
        
        last = self.queue[-1]
        for d in self.destroy:
            if d.startswith(last):
                #print "%s could react with %s"%(last,d[-1]),
                if d[-1] in self.queue:
                    #print "%s + %s = !!!BOOM!!!"%(last,d)
                    self.queue = []
                    return
                #else:
                    #print "...nothing happens" 
                
    #def print_status(self):
        #print "This is a Magicka solver..."
        #for key, val in self.combine.items():
            #print "%s + %s = %s"%(key[0],key[1],val)  
        #for d in self.destroy:
            #print "%s + %s = !BOOM!"%(d[0],d[1])
      
    def __str__(self):
        s = str(self.queue)
        return s.replace("'", "")

def solve_test(C,D,N):
    solver = MagickaSolver(C,D)
    #solver.print_status()
    #print "Invocation sequence is",N
    for el in N:
        #print "Current queue:",solver.queue
        solver.do_invoke(el)
        solver.do_combine()
        solver.do_oppose()
        #print
    
    return solver
    

    

if __name__ == '__main__':
    num_tests = int(raw_input())
    for i in range(num_tests):
        test_line = raw_input()
        data = test_line.split(" ")
        C = dict()
        D = []
        N = []
        pos = 0
        #Read combinations
        num_comb = int(data[pos])
        while(num_comb):
            pos += 1
            sc = data[pos]
            #Put A + B = C
            # and B + A = C
            C[sc[:2]]=sc[2]
            C[sc[1::-1]]=sc[2]
            num_comb -= 1
        #Read destructions
        
        pos += 1
        num_destr = int(data[pos])
        while(num_destr):
            pos += 1
            sd = data[pos]
            D.append(sd)
            D.append(sd[::-1])
            num_destr -= 1
        
        pos += 1
        num_N = data[pos]
        pos += 1
        N = data[pos]
        
        print "Case #%d: %s"%(i+1, str(solve_test(C,D,N)))
