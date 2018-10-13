class FastScanner:
    def __init__(self):
        import sys
        self.inp = map(int, sys.stdin.read().split())
        self.readAt = -1
    def nextInt(self):
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
 
def main():
    from math import log
    
    fs = FastScanner()
    pw = PrintWriter()
 
    #Input the number of test cases
    t = fs.nextInt()
    for i in xrange(t):
        row1 = fs.nextInt()
        inp = fs.nextRange(16)
        a1 = set(inp[(row1-1)*4:row1*4])
        row2 = fs.nextInt()
        inp = fs.nextRange(16)
        a2 = set(inp[(row2-1)*4:row2*4])
        answer = list(a1&a2)
        print "Case #"+str(i+1)+":",
        if len(answer)==1:
            print answer[0]
        elif len(answer)>1:
            print "Bad Magician!"
        else:
            print "Volunteer cheated!"
        
'''
This confirms that the main method is only when the
program is run. Not when the module is imported.
'''
if __name__ == "__main__":
    main() 
