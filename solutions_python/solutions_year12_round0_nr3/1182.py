import string

# Cyclically shift a string to the left by n amount
#   Changes it into a list first and then joins it back
#
#   Also look into possibility of using a deque and rotate
def shift(l,n):
    string_list = list(l)
    string_list = string_list[n:] + string_list[:n]
    return ''.join(string_list) 

test = '1234'
print shift(test, 0)
print shift(test, 1)
print shift(test, 2)
print shift(test, 3)
print shift(test, 4)
print len(test)

fin = file('C-small-attempt0.in', 'rw')
fout = file('output.txt', 'w')
               
numLine = 0   
for line in fin:
    if numLine == 0:
        numLine = numLine + 1
    else:
        fout.write('Case #' + str(numLine) + ': ')
        nums = line.strip().split(' ')
        A = nums[0] # these are strings
        B = nums[1]
        rp = 0 # number of recycled pairs
        nDigits = len(A)      

        # 1 Digit numbers won't have any recycled pairs 
        if int(B) < 10:
            fout.write('0\n')
            numLine = numLine + 1
            continue
 
        for n in range(int(A), int(B)+1):
            #print 'New Number: ' + str(i)
            for rotation in range(1, nDigits):
                nShifted = shift(str(n), rotation)
                m = int(nShifted)
                if m == n:
                    break
                if m > n and m <= int(B) and m > int(A) and m != n:
                    rp += 1

        numLine = numLine + 1
        fout.write(str(rp))
        fout.write('\n')

fin.close()
fout.close()
