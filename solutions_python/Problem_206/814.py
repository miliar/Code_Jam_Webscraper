
def main():
    # read the input file
    f = open("A-large.in", "r")
    s = f.read().split("\n")
    f.close()
    
    T = eval(s.pop(0))
    outputsStr = ""
    for i in range(T):
        D, N = [eval(ii) for ii in s.pop(0).split()]
        tmax = 0
        for j in range(N):
            K, S = [eval(ii) for ii in s.pop(0).split()]
            t = (D - K) * 1. / S
            if t > tmax: tmax = t
        
        res = D * 1. / tmax
        outputsStr += "Case #%d: %s%s" % (i+1, str(res), "\n" if i < T-1 else "")
    
    f = open("a-large.out", "w")
    f.write(outputsStr)
    f.close()

main()
