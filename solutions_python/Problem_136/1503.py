## Google Code Jam ##
## Qualification Round ##
## Problem B. Cookie Clicker Alpha ##


def run_case(line):
    nums = [float(i) for i in line.strip().split(' ')]
    c = nums[0]
    f = nums[1]
    x = nums[2]

    #print "\nStarting Case!\n"

    time = 0
    rate = 2.0
    count = 0
    done = False
    while( not done ):
        #print time, rate, count
        ## Without buying
        old_proj_time = (x - count)/rate
        
        ## With buying
        wait_time = (c - count)/rate
        new_count = 0
        new_rate = rate + f
        new_proj_time = (x - new_count)/new_rate
        total_proj_time = wait_time + new_proj_time

        if ( total_proj_time < old_proj_time ):
            time += wait_time
            rate = new_rate
            count = new_count
        else:
            time += old_proj_time
            done = True

    return '{:.8f}'.format(time)

    print "FAILED"
    sys.exit(0)

f = file('in_large.txt','r')

lines = f.readlines()

cases = int(lines[0].strip())
print "Number of cases", cases

out = file('out_large.txt','w')

for case in xrange(0,cases):
    output = run_case(lines[case+1])
    out.write("Case #" + str(case+1) + ": " + output + "\n")

f.close()
out.close()

