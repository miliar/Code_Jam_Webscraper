import sys

if __name__ == "__main__":
    output = open("B.out", 'w')
    T = int(sys.stdin.readline())
    
    for i in range(1, T+1):
        split = sys.stdin.readline().split()
        A = int(split[0])
        B = int(split[1])
        K = int(split[2])
        
        ctr = 0

        for j in range(A):
            for k in range(B):
                if j & k < K:
                    ctr += 1

        output.write("Case #%d: %d\n" %(i, ctr))
    output.close()
