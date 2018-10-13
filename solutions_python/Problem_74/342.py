import sys, os

B = []
O = []
A = []
seq = []
num = 0

def initialize(line):
    li = line.split()
    global num
    num = int(li[0])
    global oi,  bi,  B,  O,  A
    B = []
    O = []
    A = []
    for i in range(num):
        if(li[2*i+1] == 'B'):
            B.append(int(li[2*i+2]))
            A.append('B')
        elif(li[2*i+1] == 'O'):
            O.append(int(li[2*i+2]))
            A.append('O')
            
    B.append(1234)
    O.append(1234)
    
T = int(sys.stdin.readline())  
for i in range(T):
    initialize(sys.stdin.readline())
    bi = 0
    oi = 0
    op = 1
    bp = 1
    k= 0
    ans = 0
    while 1:
        flag = 0
        if op < O[oi]:
            op += 1
        elif op > O[oi]:
            op -= 1
        elif op == O[oi] and A[k] == 'O':
            k += 1
            oi += 1
            flag = 1
     
        if bp < B[bi]:
            bp += 1
        elif bp > B[bi]:
            bp -= 1
        elif bp == B[bi] and A[k] == 'B' and flag == 0:
            k += 1
            bi += 1
        
        ans += 1

        if(k >= num):
            break
        #print "op = %d, bp = %d, k = %d, O[i] = %d, B[i] = %d, A[k] = %c" % (op, bp, k,  O[oi],  B[bi],  A[k])
    print "Case #%d: %d" %( i+1, ans)
    
