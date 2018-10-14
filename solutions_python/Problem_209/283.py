from decimal import *

N = 0
K = 0
data = []

PI = Decimal(3.14159265358979323846264338327950288419716939937510)

def select_base(base):
    global N, K, data
    ret = data[base][0] * data[base][0]
    ret += data[base][2] * 2
    num = 1
    if num == K:
        return ret
    for i in range(N):
        if i != base:
            if data[i][0] <= data[base][0]:
                ret += data[i][2] * 2
                num += 1
                if num == K:
                    return ret
                
    return -1

def run():
    global N, K, data
    data = sorted(data, key=lambda x:x[2], reverse=True)

    max = Decimal(0)
    for i in range(N):
        temp = select_base(i)
        if max < temp:
            max = temp
            
    return max

fi = open("A-large.in", "r")
fo = open("a_output.txt", "w")

getcontext().prec = 50

T = int(fi.readline())
for i in range(T):
    temp = fi.readline()
    N = int(temp.split()[0])
    K = int(temp.split()[1])
    data = []
    for j in range(N):
        temp = fi.readline()
        rad = int(temp.split()[0])
        hei = int(temp.split()[1])
        data.append([rad, hei, rad * hei])

    answer = run()
    answer = Decimal(answer) * PI
    fo.write("Case #" + str(i+1) + ": " + str(answer) + "\n")
    print i

fi.close()
fo.close()
