input_file_name = 'B-small-attempt0.in'
output_file_name = 'output-small.txt'

input = [x.strip() for x in open(input_file_name, 'r')]
output = open(output_file_name, 'w')

INITIAL_RATE = 2.0

def solve(c, f, x):
    best = x / INITIAL_RATE
    
    farms = 1
    
    while True:
        score = 0
        rate = INITIAL_RATE
        
        for i in xrange(farms):
            score += c / rate
            rate += f
        score += x / rate
        
        if score < best:
            best = score
            farms += 1
        else:
            break
    
    return round(best, 7)

case_num = int(input[0])

for i in range(case_num):
    c, f, x = [float(x) for x in input[i + 1].split(' ')]
    result = solve(c, f, x)
    output.write("Case #%s: " % (i + 1))
    output.write("%s\n" % result)




