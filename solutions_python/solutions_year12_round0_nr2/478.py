# Date:2012-04-14
# Author: Chika

with open("B-large.in") as infile:
    T = int(infile.readline())

    with open("B-large.out", "w") as outfile:
        for i in range(T):
            testcase = [int(j) for j in infile.readline().split()]
            N = testcase[0]
            S = testcase[1]
            p = testcase[2]
            scores = testcase[3:]
            scores.sort()

            # the min value(may be suprising) can have a best result of greater than or equal to p.
            boundary_value = p * 3 - 4 
            suprising_value_count =  scores.count(boundary_value) + scores.count(boundary_value+1)
            if scores[-1] >= boundary_value:
                while boundary_value not in scores:
                    boundary_value += 1
                boundary_index = scores.index(boundary_value)

                ret = len(scores) - boundary_index
                if suprising_value_count > S:
                    ret -= (suprising_value_count - S)
                if (boundary_value == 0) and (p != 0):
                    ret -= scores.count(0)
                if ret < 0:
                    ret = 0
            else:
                ret = 0
                
            outfile.write("Case #%d: %d\n" % (i+1, ret, ))
