#THIS IS NOT TRUE!: Remember once the number is <=2 there is no point anymore.
input_file = "B-large"
input_file += raw_input("Input file number and file extension:\n")
output_file = "outputBlarge.txt"

import math

inp = open(input_file, 'r')
out = open(output_file, 'w')
T = int(inp.readline())
for test in range(1, T + 1):
    raw_arr = [int(item) for item in inp.readline().split()]
    [N, S, p] = raw_arr[:3]
    arr = raw_arr[3 : N + 3]
    arr.sort()
    arr = arr[::-1]
    num = 0
    for t in arr:
        if int((t + 2) / 3) >= p:
            num += 1
            #print "test ", test, ", t", t, ": not surprised" 
        elif t and t % 3 != 1 and int((t + 1) / 3) + 1 >= p:
            if S <=0:
                break
            num += 1
            S -= 1
            #print "test ", test, ", t", t, ": surprised, ", S, " surprises left" 
        else:
            break
    out.write("Case #" + str(test) + ": " + str(num) + "\n")


out.close()
inp.close()
print "Done!"
