import sys
from math import floor,ceil,log2


def bathroom(N, K):
    if K == 1:
        l = floor((N-1)/2)
        r = ceil((N-1)/2)
        return (l,r)
    else:
        logk = int(floor(log2(K)))  # logk >= 1
        #print("logk = {0}".format(logk))
        res = K % (2**logk)
        #print("res = {0}".format(res))
        temp = 2**(logk-1)
        #print("temp = {0}".format(temp))
        (l_rek, r_rek) = bathroom(N, temp+(res % temp))
        if res < temp:
            return bathroom(r_rek, 1)
        else:
            return bathroom(l_rek, 1)


if __name__ == "__main__":
    name = "C-small-2-attempt0"
    f = open("{0}.in".format(name))
    output = open("{0}.out".format(name), "w")
    #print(bathroom(4,1))
    cases = int(f.readline())
    for i in range(cases):
        #print("---------------------------")
        split = f.readline().split()
        #print(split)
        N = int(split[0])
        K = int(split[1])
        (l,r) = bathroom(N, K)
        output.write("Case #" + str(i + 1) + ": " + str(r) + " " + str(l) + "\n")
    f.close()
    output.close()
