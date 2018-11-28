import sys
testcase, j =0,0
cost_of_farm, required_cookie, farm_op = 0.0000000, 0.0000000, 0.000000
row_val = []
max_time, value = 0.0000000, 0.0000000
with open("small.in") as status:
    status.seek(0)
    testcase = int(status.readline())
    while True:
        for i in xrange(0,testcase):
           row_val = [float (x) for x in status.readline().split()]
           cost_of_farm = row_val[0]
           farm_op = row_val[1]
           required_cookie = row_val[2]
           max_time = required_cookie/2.0 
           j = 0
           while True:
               j+=1
               for m in xrange(0,j):
                   value += cost_of_farm/(2.0 + (float(m) * farm_op))
               value += required_cookie/(2.0 + (float(j)) * farm_op)
               if((max_time < value) and j == 1):
                   print "Case #%d: %f" % (i+1,max_time)
                   value = 0
                   break
               elif(max_time < value):
                   print "Case #%d: %f" % (i+1,max_time)
                   value = 0
                   break 
               elif(max_time >= value):
                   max_time = value;
                   value = 0
        else:
            status.close()
            break    
