import sys

input_line = open(sys.argv[1], 'r').read().strip().split('\n')
testcase_no = int(input_line.pop(0))
out_fp = open(sys.argv[2], 'w')

print "testcase_no %s"%(testcase_no)

def parse_testcase(lines):
    num_int = int(lines.pop(0))
#    print "num_int %s"%(num_int)
    def ret_line():
        result = list()
        line = lines.pop(0).split()
#        print "line %s"%(line)
        for i in line:
            result.append(int(i))
        return result
    x = ret_line()
    y = ret_line()
    return num_int, x, y

for cur in range(testcase_no):
    
    num_int, x, y = parse_testcase(input_line)
    x.sort()
    x.reverse()
    y.sort()

    prod = 0
    for i in range(num_int):
        prod += x[i]*y[i]


#    print "Case #%i: %i"%(cur+1, prod)
    out_fp.write("Case #%i: %i\n"%(cur+1, prod))

