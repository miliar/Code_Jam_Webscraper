def calc(ns, k):
    ret = 0
    for i in range(len(ns) - k + 1):
        if ns[i] == 0:
            for j in range(i, i+k):
                ns[j] = 1 - ns[j]
            ret += 1
        # print ns
    if 0 in ns:
        ret = "IMPOSSIBLE"
    return ret


def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('output', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        
        s = linelst[0]
        k = int(linelst[1])
        ns = [0] * len(s)
        i = 0
        for c in s:
            if c == '+':
                ns[i] = 1
            i += 1
        ret = calc(ns, k)
        
        result = "Case #" + str(case) + ": " + str(ret)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    
    main()
    

    
    