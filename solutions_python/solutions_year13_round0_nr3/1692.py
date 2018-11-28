import math
import sys

T = int(sys.stdin.readline())

all_num = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212]
 
#small 10e3
#large1 10e14
#large2 10e100
for e in xrange(3, int(math.ceil(math.log(math.floor(math.sqrt(10e14)), 10)))):
    start = pow(10, e)
    end = pow(10, e)*2
    for e1 in xrange(e):
        end += pow(10, e1)
    end += 2
    for n in xrange(start, end):
        is_n = True
        is_nsq = True
        sn = str(n)
        for j in range(len(sn)/2):
            if sn[j] != sn[-(j+1)]:
                is_n = False
                break
        if is_n:
            nsq = n*n
            snsq = str(nsq)
            for j in range(len(snsq)/2):
                if snsq[j] != snsq[-(j+1)]:
                    is_nsq = False
                    break
            if is_n and is_nsq:
                #print n, nsq
                all_num.append(n)


for i in range(T):
    s = sys.stdin.readline().strip()
    A, B = s.split(' ')
    A = int(A)
    B = int(B)
    asr = int(math.ceil(math.sqrt(A)))
    bsr = int(math.floor(math.sqrt(B)))
    #print asr, bsr, [x for x in all_num if x >= asr and x <= bsr]
    cnt = len([x for x in all_num if x >= asr and x <= bsr])
    ret = "Case #" + str(i+1) + ": " + str(cnt)
    print ret

