#!/usr/bin/env python
#coding=utf-8

problem = 'aa'
input_file_name = problem + ".in"
output_file_name = problem + ".out"
test_data = """3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
"""
test_data = None

def process(input):
    output = []
    iLine = 0
    L, D, N = map(lambda x: int(x), input[iLine].strip().split())
    iLine += 1
    
    w = []
    for i in range(D):
        w.append(input[iLine].strip())
        iLine += 1
#    print w
    
    for case in range(1, N + 1):
        print "Case %d"%case
        
        ##########################
        # Get source data here
        c = input[iLine].strip()
        iLine += 1
        cl = []
        p = 0
        for i in range(L):
            if '(' != c[p]:
                cl.append(c[p])
                p += 1
            else:
                ep = c.find(')', p)
                cl.append(c[p+1:ep])
                p = ep + 1
#        print cl
        

        ##########################
        # Solve the case here
        result = 0
        
        for s in w:
            flag = 1
            for i in range(L):
                if s[i] not in cl[i]:
                    flag = 0
                    break
            result += flag
        
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
    
