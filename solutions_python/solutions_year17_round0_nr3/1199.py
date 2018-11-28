import math

fin = open("C-small-2-attempt0.in", "r")
fout = open("C-small-2-attempt0.out", "w")

tc = int(fin.readline())
for t in range(0, tc):
    temp = fin.readline().split()
    n = int(temp[0])
    k = int(temp[1])
    kth = int(math.log(k, 2))
    pre = list()
    if n % 2 == 0:
        pre.append(int((n-1)/2))
        pre.append(int(n/2))
    else:
        pre.append(int((n-1)/2))
        pre.append(int((n-1)/2))
    pre = sorted(pre, reverse=True)
    idx = 1
    resleft = 0
    resright = 0
    # print("kth = ", kth)
    if kth == 0:
        resright = pre[1]
        resleft = pre[0]
    while True:
        if kth == 0:
            break
        print("progress = " + str(idx))
        curr = list()
        # print(pre)
        if idx == kth:
            #find result
            if pre[ k-2**kth ] % 2 == 0:
                resright = ( int( (pre[k-2**kth]-1) / 2))
                resleft = ( int( pre[k-2**kth] / 2))
            else:
                resright = ( int( (pre[k-2**kth]-1) / 2))
                resleft = ( int( (pre[k-2**kth]-1) / 2))
            break
        else:
            #list calculating
            for i in range(0, len(pre)):
                if pre[i] % 2 == 0:
                    curr.append( int( (pre[i]-1) / 2))
                    curr.append( int( pre[i] / 2))
                else:
                    curr.append( int( (pre[i]-1) / 2))
                    curr.append( int( (pre[i]-1) / 2))
            curr = sorted(curr, reverse=True)
            pre = curr
            idx = idx + 1
    #print("resleft = ", resleft, "resright = ", resright)
    fout.write("Case #" + str(t+1) + ": " + str(resleft) + " " + str(resright) + "\n")
    

fin.close()
fout.close()