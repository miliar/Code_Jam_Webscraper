import sys
import numpy as np

colors = "R O Y G B V".split()

def solve_small(n, counts):
    last = -1
    first = -1
    output = ""
    for i in range(n):
        j_max = 0
        mx = 0


        

        for j in range(len(counts)):
            if j!=last and counts[j]>mx:
                mx = counts[j]
                j_max = j
            
            elif j!=last and counts[j]==mx and j==first:
                mx = counts[j]
                j_max = j

        if mx == 0:
            return "IMPOSSIBLE"

        if i==0:
            first = j_max
        
        counts[j_max] -= 1
        last = j_max
        
        # sys.stdout.write(colors[j_max])
        output += colors[j_max]

    if(output[0]==output[-1]):
        return "IMPOSSIBLE"

    return output

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for i in xrange(t):
    	inp = np.array(f.readline().split(), 'int')

        n = inp[0]
        counts = inp[1:] 

        output = solve_small(n, counts)
		
        print("CASE #{0}: {1}".format(i+1, output))