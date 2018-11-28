'''
Created on 14/apr/2012

@author: matteo
'''


    

def count(A,B):
    nchr = len(str(A))
    maxc = pow(10,nchr) - A 
    #print maxc
    counter = A
    xcount = []
    for i in xrange(0,maxc):
        counter = A + i        
       # print counter
        for c in xrange(1,nchr):
            l = str(counter)[0:c]
            r = str(counter)[c:]
            if int(r[0]) > 0:
                m = int(r + l)
                if A <= counter < m <= B:
                    #print m
                    rec = [counter,m]
                    if not rec in xcount:
                        xcount.append(rec)
    
    return len(xcount)

def test(ifp):
    nrows = int(ifp.readline())
    ofp = open("../recycled/out.txt" ,"w")
    for i in xrange(1,nrows+1):
        line = (ifp.readline().strip())
        sline = line.split(' ')
        msg = "Case #%d: %d" % (i,count(int(sline[0]),int(sline[1]) ))
        print msg
        ofp.write(msg + '\n')
    ofp.close() 
        

if __name__ == "__main__":
    ifilename = '../recycled/C-small-attempt0.in' 
#    ifilename = '../recycled/test.in' 
    if ifilename != "":
        print ifilename
        ifp = open(ifilename, "r")        
        test(ifp)      
        ifp.close()
