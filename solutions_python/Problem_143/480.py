f = open(r'K:\Codes\code jam solutions\2014 Round 1B\Problem B New Lottery Game\B-small-attempt0.in')
out = open(r'K:\Codes\code jam solutions\2014 Round 1B\Problem B New Lottery Game\testSOL.txt','w')

tc = int(f.readline())
sollist = list()

for it in range(1,tc+1):
    cases = 0
    vals = f.readline().split()
    A = int(vals[0])
    B = int(vals[1])
    K = int(vals[2])
    
    for i in range (0,A):
        for j in range(0,B):
            win = i&j
            if win < K:
                cases += 1
            
            
    out.write('Case #'+str(it)+': '+str(cases)+'\n')
    
out.close()
f.close()
    