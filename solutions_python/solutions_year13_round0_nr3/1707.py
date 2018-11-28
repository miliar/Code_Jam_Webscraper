import math
import time
start_time = time.clock()

def isP(num):
    source = num
    target = 0
    while num > 0:
        target *= 10
        target += num % 10
        num /= 10
    return source==target


fin = open('test.in', 'r')
fout = open('test.out', 'w')
length = int(fin.readline())

for i in range(1, length+1):
    a, b = [int(x) for x in fin.readline().split()]
    print a, b
    a_root = int(math.sqrt(a))
    b_root = int(math.sqrt(b))
    count = 0
    print a_root, b_root
    if isP(a_root) and isP(a_root**2) and a_root**2 >= a:
        count += 1
        print "fount", a_root**2
    num = a_root + 1
    while num < b_root + 1:
        if isP(num) and isP(num**2):
            print "found",num**2
            count += 1
        num += 1
    fout.write("Case #" + str(i) + ": " + str(count) + "\n")

fin.close()
fout.close()

end_time = time.clock()
print "time",end_time-start_time