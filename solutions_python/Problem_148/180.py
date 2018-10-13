#! /usr/bin/env python

problem = "A"
case = "large" # "small" "large"

input_file  = "%s-%s.in" % (problem,case)
output_file = "%s-%s.out" % (problem,case)


with open(input_file, 'r') as inputf, open(output_file, 'w') as outputf:
    lines = inputf.readlines()
    N = int(lines.pop(0))
    print N
    for i in range(0,N,1):
        # do something
        D,H  = map(int,lines.pop(0).split(' '))
        
        values = map(int,lines.pop(0).split(' '))
        values.sort(reverse=True)
        print values
        total = 0
        while len(values)>0:
            a = values.pop(0)
            if (len(values)>0):
                if (values[-1] + a<=H):
                    values.pop(-1)
            total = total + 1
        outputf.write("Case #%s: %s\n" % (i+1, total))
