import sys

def msb(num):
    msb = -1
    tmp = num
    while tmp > 0:
        tmp /= 2
        msb += 1

    return msb

#f_in = open("B-large.in", "r")
f_in = open("B-small-attempt0(1).in", "r")
#f_in = open("lottery.in", "r")
f_out = open("lottery.out", "w")

size = int(f_in.readline())

for case_num in range(size):
    data = [int(x) for x in f_in.readline().strip().split()]
    A = data[0]
    B = data[1]
    K = data[2]

    total = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                total += 1
    # k_msb = msb(K)
    # a_msb = msb(A)
    # b_msb = msb(B)
    
    # total = 0
    # print k_msb
    # while True:
    #     a_sub_k_range = min(2**(k_msb), A)
    #     b_sub_k_range = min(2**(k_msb), B)

    #     total += a_sub_k_range * b_sub_k_range
    #     total *= 3
    #     break

    f_out.write("Case #" + str(case_num + 1) + ": " + str(total) + "\n")
        

f_in.close()
f_out.close()