def war():
    aa = A[::1]
    bb = B[::1]
    ret = 0
    for i in range(len(aa)):
        x = aa[i]
        flag = False
        for j in range(len(bb)):
            if(bb[j] > x):
                flag = True
                bb.remove(bb[j])
                break
        if(not flag):
            ret += 1
            bb.remove(bb[0])
    return ret

def dwar():
    aa = A[::1]
    bb = B[::-1]
    #print aa
    #print bb
    ret = 0
    for i in range(len(aa)):
        x = aa[i]
        flag = False
        for j in range(len(bb)):
            if(bb[j] < x):
                flag = True
                bb.remove(bb[j])
                ret += 1
                break
        if(not flag):
            bb.remove(bb[0])
    return ret

cas = int(raw_input().strip())

for cc in range(1,cas+1):
    N = int(raw_input().strip())
    A = raw_input().strip().split()
    B = raw_input().strip().split()

    for i in range(N):
        A[i] = float(A[i])
        A.sort()
        B[i] = float(B[i])
        B.sort()
    #print A
    #print B
    print 'Case #' + str(cc) + ': ' + str(dwar()) + ' ' + str(war())
