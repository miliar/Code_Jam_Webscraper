input = open('input2', 'r')
output = open('output2', 'w')

testcases = int(input.readline().strip())
for testcase in xrange(1, testcases+1):
    values = input.readline().strip().split(' ')
    c, f, x  = [float(x) for x in values]
    init_time = x / 2
    next_time = c/2 + x/(2+f)
    n = 0
    carry = c/2
    while init_time > next_time:
        n += 1
        init_time = next_time
        carry += c/(2+n*f)
        next_time = carry + x/(2+n*f+f)
    output.write("Case #%s: %f\n" % (testcase, init_time))

input.close()
output.close()
