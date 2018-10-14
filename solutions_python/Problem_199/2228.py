import sys
read=lambda:sys.stdin.readline().rstrip()
readi=lambda:int(sys.stdin.readline())
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
sys.stdout = open('output.txt', 'w')
with open('A-large.in') as f:
    T = int(f.readline().rstrip());
    for t in range(T):
        S,K = f.readline().split()
        K = int(K)
        ls = len(S)
        ps = [0 if c == '-' else 1 for c in S]
        c1 = 0;  flip = 0; 
        while c1 + K <= ls:
            if ps[c1]:
                c1 += 1
                continue
            nh = False; nidx = -1
            for d in range(K):
                ps[c1 + d] ^= 1
                if not nh and not ps[c1 + d]:
                    nh = True
                    nidx = c1 + d
            else:
                flip += 1

            if nh:
                c1 = nidx
            else:
                c1 += K
        
        flag = False;
        for k in range(K):
            if not ps[ls-1 - k]:
                flag = True
                break
        
        if flag:
            answer = "IMPOSSIBLE"
        else:
            answer=  flip
        
        write("Case #%d: %s\n" % (t+1, str(answer)))
sys.stdout.close()



