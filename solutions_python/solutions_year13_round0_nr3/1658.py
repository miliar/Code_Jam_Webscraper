from math import sqrt, ceil, log
import pdb

def polygen(start, end):
    num_len = len(str(start))
    start = str(start)
    if len(start) == 1:
        num = int(start)
    else:
        num = int(start[:int(ceil(len(start)/2.0))])
    next_size = min(10**(ceil(log(num + 1, 10))) - 1, end)
    if int(str(num) + str(num)[::-1][num_len %2:]) < int(start):
        num += 1
    while int(str(num) + str(num)[::-1][num_len %2:]) <= end :
        while num <= next_size and int(str(num) + str(num)[::-1][num_len %2:]) <= end:
            yield int(str(num) + str(num)[::-1][num_len %2:])
            num += 1
        num_len += 1
        num = 10**(int(ceil(num_len/2.0)) - 1)
        next_size =  10**(int(ceil(num_len/2.0))) - 1
            

def is_polyndrom(num):
    if str(num) == str(num)[::-1]:
        return True
    return False
    
def fair_and_Square2(start, end):
    count = 0
    #start = int(ceil(sqrt(start)))
    #end = int(sqrt(end))
    len_min = len(str(start))
    len_max = len(str(end))
    for num in xrange(start, end + 1):
        if is_polyndrom(num):
            if sqrt(num).is_integer() and is_polyndrom(int(sqrt(num))):
                print num
                count += 1
    return count

def fair_and_Square(start, end):
    count = 0
    start = int(ceil(sqrt(start)))
    end = int(sqrt(end))
    #len_min = len(str(start))
    #len_max = len(str(end))
    for num in polygen(start, end):
        if is_polyndrom(num**2):
            #print num*num
            #print num
            count += 1
    return count
    

def main(args):
    out_string = "Case #%d: %d\n"
    f = open(args[1])
    out = open(args[1]+".out.txt", 'wt')
    number_of_cases = int(f.readline().strip())
    for i in xrange(number_of_cases):
        start, end = (int(j) for j in f.readline().split())
        print out_string % (i + 1, fair_and_Square(start, end))
        out.write(out_string % (i + 1, fair_and_Square(start, end)))
    f.close()
    out.close()

if "__main__" == __name__:
    import sys
    import time
    start = time.time()
    main(sys.argv)
    print time.time() - start