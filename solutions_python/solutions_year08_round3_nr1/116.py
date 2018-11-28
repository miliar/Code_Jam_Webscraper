import sys

def A(filename):
    f = open(filename,'rb')
    line = f.readline()
    N = int(line.rstrip()) # N is the number of test cases
    results = []
    for i in range(N):
        line = f.readline()
        P,K,L =[int(a) for a in line.rstrip().split(' ')] # P is letters on a key, K is keys, L is letters
        line = f.readline()
        letters = [int(a) for a in line.rstrip().split(' ')]
        letters.sort()
        letters.reverse()
        pattern = [[0]*P]*K
        l = 0
        result = 0
        for j in range(P):
            for k in range(K):                
                result += letters[l]*(j+1)
                l +=1
                if (l >= L): break;
            if (l >= L): break;
        results.append(result)

    k = 1
    for result in results:
        print "Case #%d: %d" % (k,result)
        k+=1
    f.close()

if __name__ == '__main__':
    A(sys.argv[1])
