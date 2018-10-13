import sys

def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file)
        numOfTest = f.readline().split()[0]
        for k in range(int(numOfTest)):
            Nums = f.readline().split()
            A = int(Nums[0])
            B = int(Nums[1])
            K = int(Nums[2])
            n = 0
            for i in range(A):
                for j in range(B):
                    if success(i,j,K):
                        n+=1
            print "Case #" + str(k+1) + ": " + str(n)
            
def success(i,j,k):
    c = i & j
    return c <k

if __name__ == '__main__':
    main()