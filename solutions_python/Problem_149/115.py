# ?

#file_in = "B-sample.in"
#file_out = "B-sample.out"
file_in = "B-small-attempt1.in"
file_out = "B-small-attempt1.out"
#file_in = "B-large.in"
#file_out = "B-large.out"

#import math

# Solves the problem
def Solve(N, A):
    SA = sorted(A)
    
    f = []
    b = []

    count = 0
    for a in SA:
        i = A.index(a)
        cf = 0
        cb = 0
        if 0 == i or N - 1 == i:
            continue
        for j in range(0, i):
            if A[j] > a:
                cf = cf + 1
        for j in range(i + 1, N):
            if A[j] > a:
                cb = cb + 1
        count = count + min(cf, cb)
    return count



# Reads the input data and runs the test cases
def Run():
    fin = open(file_in, 'r')
    fout = open(file_out, 'w')

    lines = []
    for l in fin:
        lines.append(l)

    i = 0
    T = int(lines[0])
    i = i + 1
    
    for tc in range(0, T):
        N = int(lines[i].rstrip())
        i = i + 1
        As = lines[i].rstrip().split(' ')
        i = i + 1
        A = []
        for j in xrange(0, N):
            A.append(int(As[j]))
        result = str(Solve(N, A))
        fout.write("Case #" + str(tc + 1) + ": " + result + '\n')
    fin.close()
    fout.close()
    

def main():
    Run()

if __name__ == "__main__":
    main()
