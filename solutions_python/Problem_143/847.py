f = open('B-small-attempt3.in', 'r')
#f = open('B-small.txt', 'r')
#f = open('B.txt', 'r')
testcases = f.readline()
testcases = int(testcases)

f2 = open('outputB.txt','w')


for x in range(1, testcases+1):
    line = f.readline()
    line = [int(k) for k in line.split(' ')]
    A = line[0]
    #A_bin = int(bin(line[0])[2:])
    B = line[1]
    #B_bin = int(bin(line[1])[2:])
    K = line[2]  
    counter = 0
    #print "A: ", A, "B: ", B
    #print "A and B: ", A_bin&B_bin
    #print "A_bin: ", A_bin, "B_bin: ", B_bin
    #print "A AND B : ", A & B
    for a in range (0, A):
        for b in range (0, B):
            if ((a & b) < K ):
                counter = counter + 1
   
    if x == testcases:    
        print "Case #%d: %d" % (x,counter)
        f2.write("Case #%d: %d" % (x,counter));
        
    if x<testcases:
        print "Case #%d: %d\n" % (x,counter)
        f2.write("Case #%d: %d\n" % (x,counter));
   
   
   
   
   
   
   
   
#==============================================================================
#     if x == testcases:    
#         #print "Case #%d: %.7f" % (x,oldtime)
#         f2.write("Case #%d: " % (x,oldtime));
#         
#     if x<testcases:
#         #print "Case #%d: %.7f\n" % (x,oldtime)
#         f2.write("Case #%d: \n" % (x,oldtime));
#==============================================================================
        
    
f2.close()
f.close()