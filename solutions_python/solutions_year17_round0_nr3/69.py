
def f(n,k):
    numOfBlocks = 2**(k.bit_length()-1)
    blockSize = (n - numOfBlocks + 1)// numOfBlocks

    if n - blockSize*numOfBlocks >= k:
        blockSize += 1

    return [blockSize//2, (blockSize-1)//2]
        

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    m1,m2 =  f(n,k)
    print('Case #' + str(i+1) + ':', m1, m2)
    

