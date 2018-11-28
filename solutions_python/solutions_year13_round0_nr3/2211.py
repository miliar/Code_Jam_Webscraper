# -*- coding: utf-8 -*-

import math
import sys

def _is_square(integer):
    root = math.sqrt(integer)
    
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False
    

in_file = sys.argv[1]
out_file = in_file.replace(".in", ".out")

f_in = open(in_file, "rt")
f_out = open(out_file, "wt")

case = 1

next(f_in)

for line in f_in:
    line = line.strip()
    
    numbers = 0
    start, end = line.split()
    start = int(start)
    end = int(end)
    
    print("%s - %s" % (start, end))
    
    for i in range(start, end + 1):
        s = str(i)
        
        if s == s[::-1] and _is_square(i):
            root = int(math.sqrt(i))
            
            if str(root) == str(root)[::-1]:
                print(i)
                numbers += 1
    
    print("")
    f_out.write("Case #%s: %s\n" % (case, numbers))
    
    case += 1

f_in.close()
f_out.close()
