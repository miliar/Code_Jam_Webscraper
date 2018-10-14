"""
username: TheGanis 
email: ganiszulfa [at] gmail [dot] com
"""
#!/usr/bin/python

import sys

if len(sys.argv) < 2:
    print 'WARNING..........!!!not enough args'
    sys.exit() 
 
inp = open(sys.argv[1], "r")
inp = inp.readlines()
outp = open('output.txt', "w")
line_no = 0

def read():
    global line_no, inp
    ret = inp[line_no].rstrip()
    line_no+=1
    return ret

cases = int(read())

# start code here

for c in range(cases):
    line = str(read())
    line = line.split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    t = 'notenoughtrange'
    f = 2
    e = 0

    for i in range(0,999999): 
        wait = X/f
        build = C/f + X/(f+F) 
        if wait<=build:
            t = wait + e
            break
        e += C/f
        f += F
    
    print 'Case #',c+1, ': ' , t
    outp.write('Case #%d: %.6f\n' % (c+1, t))

# end code here
outp.close()
