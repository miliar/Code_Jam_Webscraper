import math

if __name__ == '__main__':
    input = open('./source/C-large-0.in', 'r')
    output = open('./source/C-large-0.out', 'w')

    n = int(input.readline().strip())
    for i in range(n):
        input.readline()
        seq = input.readline().strip().split()
        sum_xor = summ = minm = int(seq[0])
        j = 1
        while j < len(seq):
            v = int(seq[j])
            sum_xor ^= v
            summ += v
            if v < minm:
                minm = v
            j += 1
        if sum_xor != 0:
            print >>output, "Case #%d: NO" % (i+1)
        else:
            print >>output, "Case #%d: %d" % (i+1, summ-minm)
        
