from fractions import gcd
INPUT_FILE = 'inputs/B-large.in'
OUTPUT_FILE = 'outputs/B-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

C = int(f_in.readline())
for c in range(C):
    t = [int(i) for i in f_in.readline().split()]
    N = t[0]
    t = t[1:] # cut off the number of elements
    diffSet = set()
    for i in range(N - 1):
        diffSet.add(abs(t[i] - t[i + 1]))
            
    tmpGcd = diffSet.pop();
    setSize = len(diffSet)
    for d in range(setSize):
        tmpElem = diffSet.pop();
        tmpGcd = gcd(tmpElem, tmpGcd)
    
    y = 0
    if (t[0] % tmpGcd) != 0:
        y = tmpGcd - (t[0] % tmpGcd)
    strRes = "Case #" + str(c + 1) + ": " + str(y)
    f_out.write(strRes + "\n")
    print(strRes)

f_in.close()
f_out.close() 