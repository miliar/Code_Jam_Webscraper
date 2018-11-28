import itertools

def find(d):
    for su in d.values():
        for i in xrange(0,len(su)):
            for j in xrange(i+1,len(su)):
                if len(su[i] - su[j]) == len(su[i]):
                    return su[i], su[j]
    return None
                    
with open('C-small-attempt0.in') as f:
    N = int(f.readline())
    out = file('testC.out','w')
    for n in range(1, N+1):
        d = {}
        line = map(int, f.readline().strip().split())
        for r in xrange(1,21):
            for a in itertools.combinations(line[1:], r):
                
                a = set(a)
                su = sum(a)
                if su not in d:
                    d[su] = [a]
                else:
                    d[su].append(a)
        ans = find(d)
        
        
        if ans!= None:
            out.write("Case #"+str(n)+":\n")
            part1 = map(str, ans[0])
            part2 = map(str, ans[1])
            out.write(" ".join(part1)+"\n")
            out.write(" ".join(part2)+ "\n")
            
                        
            
        
        
        
        
        #out.write('Case #%i: %s\n'%(n,' '.join(R)))
        
    out.close()
    
