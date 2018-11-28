import time

in_file = "B-large.in"
out_file = "B-large.out"

def start():
    f_in = file(in_file, "r")
    f_out = file(out_file, "w")    
    T = int(f_in.readline().strip())

    for i in xrange(T):
        N = int(f_in.readline().strip())
        next_num = getNextNum(N);
        f_out.write("Case #" + str(i+1) + ": " + str(next_num) + "\n")
        print "for i: ", i, " next num is: ", next_num

    f_in.close()
    f_out.close()

def getNextNum(N):
    digits = []    
    no = N
    while no:
        digits.append(no%10)
        no = int(no/10)
    digits.reverse()

    sortDgts = digits[::]
    sortDgts.sort()
    sortDgts.reverse()

    size = len(digits)
    if digits == sortDgts:
        sortDgts.reverse()
        count = 0
        for i in xrange(size):
            if sortDgts[i] == 0:
                count = count+1
            else:
                break
        digits = []
        digits.append(sortDgts[count])
        for i in xrange(count+1):
            digits.append(0)
        for i in xrange(count+1, size):
            digits.append(sortDgts[i])
            
    else:
        zeroC = 0
        for i in xrange(size):
            if digits[size-1-i] == 0:
                zeroC = zeroC + 1
            else:
                break
        if zeroC != 0:
            size = size-zeroC
            digits = digits[0:size]
        
        flag = False
        for i in xrange(size-1):
            #print "size-i-1: ", size-i-1
            if flag:
                break
            l1 = digits[size-i-2]
            for j in xrange(i+1):
                #print "size-i-2-j: ", size-i-2-j
                #l2 = digits[size-i-1-j]
                l2 = digits[size-1-j]
                #print l1, l2
                if l2 > l1:
                    #print "digits before: ", digits
                    #print "to delete: ", size-i-1
                    del digits[size-1-j]
                    #print "digits after: ", digits
                    digits.insert(size-i-2, l2)
                    indx = size-i-2+1+zeroC
                    if zeroC:
                        for k in xrange(zeroC):
                            digits.insert(size-i-2+1+k, 0)

                    if not indx >= len(digits)-1:
                        last = digits[indx:]
                        last.sort()
                        digits = digits[0:indx]
                        digits = digits + last                        
                    #print "digits after insert: ", digits
                    flag = True
                    break    

    num = 0
    for i in xrange(len(digits)):
        num = num*10 + digits[i]
    return num       
    
start()   
           
