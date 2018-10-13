import sys

def main():
    infile = open('A-large.in', 'r');
    cases = int(infile.readline());
    f = open('A-large.out', 'w')
    for case in range(1, cases+1):
        ans = 0
        line = infile.readline().strip().split();
        
        N = int(line[0])
        R, P = [], []
        As = []
        Bs = []
        aPos = 1
        bPos = 1
        for n in range(0,N):
            r = line[1+n*2]
            p = int(line[1+n*2+1])
            R.append(r)
            P.append(p)
            if r == 'O':
                As.append(abs(aPos - p))
                aPos = p
            else:
                Bs.append(abs(bPos - p))
                bPos = p
            
        
        aPos = 1
        bPos = 1
        
        buttons = zip(R,P)
        
        distA = 0
        distB = 0
        
        nextB = 0
        nextA = 0
        for idx, button in enumerate(buttons):
            if button[0] == 'O':
                dist = max(0,As[nextA] - distA) + 1
                ans += dist
                distB += dist
                distA = 0
                nextA += 1
            else:
                dist = max(0,Bs[nextB] - distB) + 1
                ans += dist
                distA += dist
                distB = 0
                nextB += 1
            
        s = "Case #%d: %d\n" % (case, ans)
        print s,
        f.write(s)
    
    f.close()
main();