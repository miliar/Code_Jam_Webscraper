class FastScanner:
    def __init__(self):
        import sys
        self.inp = map(float, sys.stdin.read().split())
        self.readAt = -1
    def nextFloat(self):
        self.readAt += 1
        return self.inp[self.readAt]
    def nextRange(self, n):
        self.readAt += n
        return self.inp[self.readAt-n+1:self.readAt+1]
 
class PrintWriter:
    def __init__(self):
        self.pw = []
    def println(self, n):
        self.pw.append(n)
    def flush(self):
        print "\n".join(map(str, self.pw))

def roundOff(num):
    import decimal
    return round(decimal.Decimal(str(num)),2)

def main():
    from math import log
    
    fs = FastScanner()
    pw = PrintWriter()
 
    #Input the number of test cases
    t = int(fs.nextFloat())
    for i in xrange(t):
        rate = 2.0
        c,f,x = fs.nextRange(3)
        ans = x/rate
        runCount = 0
        time2 = 0
        print "Case #"+str(i+1)+":",
        while True:
            runCount += 1
            time1 = x/rate
            time2 += c/rate
            val = time2 + x/(rate+f)
            #print ans,val
            if ans>val:
                ans = val
            else:
                print "%.7f" % ans #round(ans,7)
                break
                #print ans, rate, f
            rate += f
            #if runCount==5: break
        
'''
This confirms that the main method is only when the
program is run. Not when the module is imported.
'''
if __name__ == "__main__":
    main() 
