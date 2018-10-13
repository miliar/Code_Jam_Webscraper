import sys

INPUT_NAME = sys.argv[1]
OUTPUT_NAME = sys.argv[2]

f = open(INPUT_NAME,'r')
out = open(OUTPUT_NAME,'w')

num_cases = int(f.readline().strip())

for test in range(num_cases):
    def flip(p,k,i):
        for j in range(i,i+k):
            if p[j] == "+":
                p[j] = "-"
            else:
                p[j] = "+"
        return p

    p_string,k_string = f.readline().strip().split(" ")
    p = list(p_string)
    k = int(k_string)
    n = 0
    i = 0
    while '-' in p and i <= len(p)-k:
        if p[i] == "-":
            p = flip(p,k,i)
            n += 1
        i += 1


    if '-' in p:
        out.write("Case #%d: IMPOSSIBLE\n" % (test+1))
    else:
        out.write("Case #%d: %d\n" % (test+1,n))
