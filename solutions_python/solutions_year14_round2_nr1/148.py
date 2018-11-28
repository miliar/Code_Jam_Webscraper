import sys

def decompose(s):
    seq = ""
    decomp = []

    if len(s) == 1:
        return s, [1]

    cur = s[0]
    idx = 1
    ctr = 1

    while idx < len(s):
        seq += cur
        #if idx == len(s):
        #    decomp.append(ctr)
        #    break

        while s[idx] == cur:
            idx += 1
            ctr += 1
            if idx == len(s):
                break
        decomp.append(ctr)
        if idx == len(s):
            break
        cur = s[idx]
        ctr = 1
        idx += 1
    

    return seq, decomp

if __name__ == "__main__":
    output = open("A.out", 'w')
    T = int(sys.stdin.readline())
    
    for i in range(1, T+1):
        N = int(sys.stdin.readline())
        strs = []
        decomps = []
        finish = False

        for j in range(N):
            in_str = sys.stdin.readline()
            seq, decomp = decompose(in_str)

            #print seq
            #print len(seq)
            #print decomp

            if j == 0:
                standard = seq
                
            if seq != standard and not finish:
                output.write("Case #%d: Fegla Won\n" %(i))
                finish = True
            
            decomps.append(decomp)
        
        if not finish:
            ctr = 0
            for j in range(len(decomps[0])):
                l = []
                for k in range(N):
                    l.append(decomps[k][j])
                    l.sort()
                    
                mid = l[len(l) / 2]
                    
                for s in range(len(l)):
                    ctr += abs(l[s] - mid)

            output.write("Case #%d: %d\n" %(i, ctr))
    output.close()
            
            
