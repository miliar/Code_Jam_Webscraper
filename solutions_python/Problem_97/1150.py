from math import log
from math import floor
from math import pow

infile = open("C-small-attempt1.in")
outfile = open("C-small-attempt1.out", "w")

#infile = open("C.input.txt")
#outfile = open("C.output.txt", "w")

n = int(infile.readline())

def get_num_digits(num):
    return int(floor(log(num,10))+1)

for casenum in range(0, n):
    
    nums = [int(s) for s in infile.readline().strip().split(" ")]
    
    A = nums[0]
    B = nums[1]

    cnt = 0
    pairs = set()
    for i in range(A,(B+1)):
        
        num_digits = get_num_digits(i)
        ten_pow = pow(10, num_digits-1)
                 
        # rotate n times
        rotated = i
        for num_rot in range(1, num_digits):
   
            left_digit = int(floor(rotated/ten_pow))
            if left_digit==0:
                continue
            rotated = (rotated - (left_digit * ten_pow)) * 10 + left_digit

            if get_num_digits(rotated)!=num_digits:
                continue
            if rotated!=i and (A<=rotated and rotated<=B):

                if i<rotated:
                    pair = (i,rotated)
                else:
                    pair = (rotated, i)
                if pair not in pairs:
                    #print ("%d, %d" % (i, rotated))
                    cnt+=1
                    pairs.add(pair)
    outfile.write("Case #%d: %d\n" % (casenum+1,cnt))

print ("ok")

infile.close()
outfile.close()
