
def solve(M):
    WP = []
    OWP = []
    OOWP = []
    for m in M:
        WP.append((len([mm for mm in m if mm=='1']), len([mm for mm in m if mm!='.'])))
    for i in range(len(M)):
        owp = []
        for j in range(len(M)):
            if j!=i:
                wp = WP[j]
                if M[i][j]=='1':
                    owp.append((wp[0], wp[1]-1))
                elif M[i][j]=='0':
                    owp.append((wp[0]-1, wp[1]-1))
        OWP.append(owp)
        
    OWP = [ddiv(owp) for owp in OWP]
    for i in range(len(M)):
        oowp = []
        for j in range(len(M)):
            if j!=i:
                if M[i][j]!='.':
                    oowp.append(OWP[j])
        OOWP.append(oowp)
    WP = [wp[0]/wp[1] for wp in WP]
    OOWP = [sum(oowp)/len(oowp) for oowp in OOWP ]
    
    result = [((0.25*WP[i]) + (0.5*OWP[i])+(0.25 * OOWP[i])) for i in range(len(WP))]
    return result

def div(a):
    return a[0]/a[1]

def ddiv(a):
    t = [div(aa) for aa in a]
    return sum(t) / len(t)

input_file = 'A-large.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N = int(fin.readline())
    M = [fin.readline().strip() for i in range(N)]
    ans = 'Case #%d:\n%s\n'%(t, '\n'.join([str(m) for m in solve(M)]))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()