#!/usr/bin/env python

verbose = True

def log(s):
    global verbose
    if verbose:
        print(s)

class Test(object):
    def __init__(self,filename):
        self.cases = []
        with open(filename) as f:
            lines = f.readlines()
            num = int (lines[0].strip())
            for line in lines[1:]:
                line = line.strip()
                if line:
                    log(line)
                    self.cases.append(int(line))
                
        assert num == len(self.cases)
    
    def solve(self):
        i=1
        for case in self.cases:
            answer = nextnum_long(case)
            if answer is None:
                answer = str(case)+'0'
            print "Case #%s: %s" % (i,answer)
            i+=1

def nextnum_long(num):
    s = str(num)
    digits = {}
    for digit_s in s:
        if digit_s!='0':
            if digit_s not in digits:
                digits[digit_s]=0
            
            digits[digit_s]+=1

    log(digits)
    while True:
        num = num+1
        log(" checking: %s" % num)
        if match(num,digits):
            return num

def match(num,digits_m):
    s = str(num)
    digits = {}
    for digit_s in s:
        if digit_s!='0':
            if digit_s not in digits:
                digits[digit_s]=0
            
            digits[digit_s]+=1
    
    for d in digits:
        if d not in digits_m:
            return False
        if digits[d] != digits_m[d]:
            return False
    for d in digits_m:
        if d not in digits:
            return False
        if digits[d] != digits_m[d]:
            return False
    
    return True

def nextnum(num):
    s = str(num)
    digits = []
    for digit_s in s:
        digits.append(int(digit_s))
        
    log(digits)
    
    for i in xrange(len(digits)-1,0,-1):
        if digits[i]>0:
            for j in xrange(i,-1,-1):
                if digits[i] > digits[j] and digits[j] > 0:
                    tmp = digits[i]
                    digits[i]=digits[j]
                    digits[j] = tmp
                    s = ''
                    for d in digits:
                        s+=str(d)
                    return s
                
                
                
        
    pass
        
if __name__=="__main__":
    import sys
    verbose = False
    Test(sys.argv[1]).solve()