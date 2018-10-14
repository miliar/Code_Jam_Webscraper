#!/usr/bin/env python
#coding=utf-8

problem = 'bb'
input_file_name = problem + ".in"
output_file_name = problem + ".out"
test_data = """3
3
3 0 -4 0 0 3
-3 -2 -1 3 0 0
-3 -1 2 0 3 0
3
-5 0 0 1 0 0
-7 0 0 1 0 0
-6 3 0 1 0 0
4
1 2 3 1 2 3
3 2 1 3 2 1
1 0 0 0 0 -1
0 10 0 0 -10 -1
"""
test_data = None

def process(input):
    output = []
    iLine = 0
    N = int(input[iLine].strip())
    iLine += 1
    for case in range(1, N + 1):
        print "Case %d"%case
        
        ##########################
        # Get source data here
        nn = int(input[iLine].strip())
        iLine += 1
        x = []
        y = []
        z = []
        vx = []
        vy = []
        vz = []
        for i in range(nn):
            _x, _y, _z, _vx, _vy, _vz = map(lambda a: int(a), input[iLine].strip().split())
            iLine += 1
            x.append(_x)
            y.append(_y)
            z.append(_z)
            vx.append(_vx)
            vy.append(_vy)
            vz.append(_vz)
#        print x
#        print y
#        print z
#        print vx
#        print vy
#        print vz

        ##########################
        # Solve the case here
        result = 0
        
        NcxA = 0
        NcxB = 0
        NcyA = 0
        NcyB = 0
        NczA = 0
        NczB = 0
        for i in range(nn):
            NcxA += vx[i]
            NcxB += x[i]
            NcyA += vy[i]
            NcyB += y[i]
            NczA += vz[i]
            NczB += z[i]
        
        NcxA /= 1.*nn
        NcxB /= 1.*nn
        NcyA /= 1.*nn
        NcyB /= 1.*nn
        NczA /= 1.*nn
        NczB /= 1.*nn
        
        NA = NcxA**2 + NcyA**2 + NczA**2
        NB = (NcxA*NcxB + NcyA*NcyB + NczA*NczB)*2
        NC = NcxB**2 + NcyB**2 + NczB**2
#        print NA, NB, NC
        if 0 == NA:
            t = 0
        else:
            t = -NB/(2.*NA)
        if t < 0:
            t = 0
#        print t
        Nd2 = NA*t**2 + NB*t + NC
        if Nd2 < 0:
            Nd2 = 0
#        d = (Nd2/nn**2)**0.5
        d = Nd2**0.5
        result = "%.8f %.8f"%(d, t)
        
        output.append(result)
        ##########################
        
        
    return output

def main():
    input = None
    if test_data is None:
        ifile = open(input_file_name)
        input = ifile.readlines()
        ifile.close()
    else:
        input = test_data.split('\n')
        
    output = process(input)
    
    if test_data is None:
        ofile = open(output_file_name, 'w')
        for i in range(len(output)):
            print >> ofile, "Case #%d:"%(i + 1), output[i]
        ofile.close()
    for i in range(len(output)):
        print "Case #%d:"%(i + 1), output[i]
        
    return len(output)
        
if __name__ == "__main__":
    import time
    start = time.time()
    N = main()
    print "Done in %f seconds"%(time.time() - start)
    print "Average %f milliseconds"%((time.time() - start) * 1000 / N)
    
