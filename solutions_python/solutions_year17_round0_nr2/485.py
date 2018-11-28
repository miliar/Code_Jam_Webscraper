def tidyNum(Nstr):
    while True:
        res = Nstr[0]
        isValid = True
        for i in range(1, len(Nstr)):
            if Nstr[i] >= res[-1]: res += Nstr[i]
            else:
                res = res[:-1] + str(eval(res[-1]) - 1)
                res += "9" * (len(Nstr) - len(res))
                isValid = False
                break
        if res[0] == "0" and len(res) > 1: res = res[1:]
        
        Nstr = res
        if isValid: break
    
    return Nstr

def main():
    # read the input file
    f = open("B-large.in", "r")
    s = f.read().split("\n")
    f.close()
    
    T = eval(s.pop(0))
    outputsStr = ""
    for i in range(T):
        N = s.pop(0)
        res = tidyNum(N)
        outputsStr += "Case #%d: %s%s" % (i+1, str(res), "\n" if i < T-1 else "")
    
    f = open("b-large.out", "w")
    f.write(outputsStr)
    f.close()

main()
