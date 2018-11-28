import sys
testcase =0
occ1, occ2, count = 0, 0, 0
first_row, second_row, inter = [], [], []
with open("small.in") as status:
    status.seek(0)
    testcase = int(status.readline())
    while True:
        for i in xrange(0,testcase):
            occ1 = int(status.readline())
            for l in 1,2,3,4:
                if l == occ1:
                    first_row= [int (x) for x in status.readline().split()]
                else:
                    status.readline()
            occ2 = int(status.readline())    
            for l in 1,2,3,4:
                if l == occ2:
                    second_row=[int (x) for x in status.readline().split()]
                else:
                    status.readline()
            inter = filter(lambda x:x in first_row, second_row)
            count = 0
            for x in inter:
                count+=1
            if count > 1:
                print "Case #%d: Bad magician!" % (i+1)
            elif count < 1:
                print "Case #%d: Volunteer cheated!" % (i+1) 
            else:
                print "Case #%d: %d" % (i+1, inter[0])
        else:
            status.close()
            break    
