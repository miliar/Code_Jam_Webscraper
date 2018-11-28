INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())

for t in range(T):
    N = int(f_in.readline())
    A = []
    B = []
    knots = 0
    for n in range(N):
        a, b = [int(i) for i in f_in.readline().split()]
        A.append(a)
        B.append(b)
    for n in range(N):
        a = A[n]
        b = B[n]
        for k in range(N):
            if (a < A[k] and b > B[k]) or (a > A[k] and b < B[k]):
                knots += 1
                
    strRes = "Case #" + str(t + 1) + ": " + str(knots // 2)
    f_out.write(strRes + "\n")
    print(strRes) 

f_in.close()
f_out.close()
