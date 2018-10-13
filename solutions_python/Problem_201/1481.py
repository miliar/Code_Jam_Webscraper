import Queue
from math import ceil, floor, log

def stalls(input_file, output_file):
    T = int(input_file.readline())

    for case in xrange(1, T + 1):
        N, K = map(int, input_file.readline().split(' '))
        height = ceil(log(K + 1, 2)) - 1
        max_gap = ceil((N + 1)/ 2**height - 1)
        extra = max_gap * 2**height + 2**height - N
        if K <= 2**(height + 1) - extra:
            temp = max_gap
        else:
            temp = max_gap - 1
        temp = (temp - 1) / 2.0
        output_file.write("Case #" + str(case) + ": " + str(int(ceil(temp))) + " " + str(int(floor(temp))) + "\n")

#import sys
#stalls(sys.stdin, sys.stdout)

input_file = open("C:\\Users\\doritm\\Desktop\\C-small-2.in", "r")
output_file = open("C:\\Users\\doritm\\Desktop\\C-small-2.out", "w")
stalls(input_file, output_file)
input_file.close()
output_file.close()

