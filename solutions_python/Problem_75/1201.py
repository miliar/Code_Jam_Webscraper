
inp = open('B-large-0.in', 'r')
outp = open('B-large-0.out', 'w')

num = int(inp.readline())

for i in range(1, num+1):
    
    outp.write('Case #%d: ' % i)
    
    chunk = inp.readline().split()
    
    c = int(chunk[0])
    if c == 0: combines = []
    else: combines = chunk[1:c+1]
    
    d = int(chunk[c+1])
    if d == 0: opposes = []
    else: opposes = chunk[c+2:c+2+d]
    
    n = int(chunk[c+d+2])
    
    l = list(chunk[c+d+3])
    s = []
    
    for e in l:
        s.append(e)
        
        if len(s) >= 2:
            a = s.pop()
            b = s.pop()
            combined = False
            for g in combines:
                if (a == g[0] and b == g[1]) or (a == g[1] and b == g[0]):
                    s.append(g[2])
                    combined = True
                    break
            if combined == False:
                s.append(b)
                opposed = False
                for d in s:
                    for v in opposes:
                        if (d == v[0] and a== v[1]) or (d == v[1] and a== v[0]):
                            opposed = True
                            s = []
                            break
                if opposed == False:
                    s.append(a)
    
    outp.write('[')
    for i in xrange(len(s)):
        if i != 0:
            outp.write(', ')
        outp.write(s[i])
    outp.write(']')
    outp.write('\n')

outp.close()
inp.close()
