import math
INPUT_FILE = 'inputs/B-large.in'
OUTPUT_FILE = 'outputs/B-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())

for t in range(T):
    L, P, C = [int(i) for i in f_in.readline().split()]
    ans = math.log(math.log(P/L, C), 2)
    ans = math.ceil(ans)
    if (ans < 0):
        ans = 0
           
    strRes = "Case #" + str(t + 1) + ": " + str(ans)
    f_out.write(strRes + "\n")
    print(strRes) 

f_in.close()
f_out.close()
