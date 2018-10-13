def solve(p,k,freq):
    count = 0
    line = 1
    f = 0
    num = 0
    freq.sort()
    while len(freq) > 0: 
        for i in xrange(k): 
            if len(freq) == 0:  
                break 
            f = freq.pop()   
            count += line * int(f)
        line += 1
    
    return count          
 
if __name__ == '__main__':
    cases = int(raw_input())
    for i in xrange(cases):
         line = raw_input()
         data = line.split()
         line = raw_input()
         data1 = line.split()
         freq = map(int,data1)
         print "Case #%d: %d" % (i+1,solve(int(data[0]),int(data[1]),freq))