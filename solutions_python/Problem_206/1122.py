

def calc(D, mh):


    return D / mh

def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('output', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        
        D = int(linelst[0])
        N = int(linelst[1])
        mh = 0

        for i in range(N):
            line = inpfile.readline().strip()
            linelst = line.split()
            K = int(linelst[0])
            S = float(linelst[1])
            mh = max(mh, (D-K) / S)

        ret = calc(D, mh)
        
        result = "Case #%s: %.6f\n" % (case, ret)
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()



if __name__ == "__main__":
    
    main()
    
