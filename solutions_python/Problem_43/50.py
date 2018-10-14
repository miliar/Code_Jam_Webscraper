#!/usr/bin/env python
#coding=utf-8

problem = 'aa'
input_file_name = problem + ".in"
output_file_name = problem + ".out"
test_data = """4
11001001
cats
zig
111111111
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
        ss = input[iLine].strip()
        iLine += 1
        print ss
        
        

        ##########################
        # Solve the case here
        result = 0
        dd = dict()
        nset = set(range(40))
        c = ss[0]
        dd[c] = 1
        nset.remove(1)
        for c in ss[1:]:
            if c not in dd:
                mi = min(nset)
                dd[c] = mi
                nset.remove(mi)
        bb = len(dd)
        if 1 == bb:
            bb = 2
        sl = list(ss)
#        sl.reverse()
#        print "base", bb
        for x in sl:
            result *= bb
            result += dd[x]
#            print dd[x]
        print "r:",result
        
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
    
