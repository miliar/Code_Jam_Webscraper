#!/usr/bin/python
import os
def solve(exist, new):
    mkdir = 0
    fs = []
    print exist, new
    for dir in exist:
        file = os.path.basename(dir) 
        parent = os.path.dirname(dir) 
        while file != "":
            fs.append((parent, file))
            file = os.path.basename(parent) 
            parent = os.path.dirname(parent) 
    print "---", fs
    for dir in new:
        file = os.path.basename(dir) 
        parent = os.path.dirname(dir) 
        while file != "":
            if (parent, file) not in fs:
                mkdir = mkdir + 1
                print "mkdir", parent, file
                fs.append((parent, file))
            file = os.path.basename(parent)
            parent = os.path.dirname(parent) 
    
    print "----", fs 
    return mkdir 
    

def main():
    """docstring for main"""
    input = open("problem")
    ilines = [l.strip() for l in input.readlines()]
    num_tests = int(ilines[0], 0)
    ans = file("answer", "w")
    line_num = 1
    for test in xrange(num_tests):
        line = ilines[line_num]
        line_num = line_num + 1
        (n, m) = [int(x, 0) for x in line.split()]
        exist = ilines[line_num:line_num + n]
        line_num = line_num + n
        new = ilines[line_num:line_num + m]
        line_num = line_num + m
        a = "Case #%d: %d\n" % (test + 1, solve(exist, new))
        ans.write(a)
        print a
    ans.close()

if __name__ == '__main__':
    main()        
