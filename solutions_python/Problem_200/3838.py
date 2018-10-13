
f = open('B-large.in','r')
w = open('B-large-attempt0.txt','w')
T = int(f.readline())

def check(B):
    C = B[:]
    C.sort()
    if B == C:
        return True
    return False

for i in range(0, T):
    N = int(f.readline())
    B = map(int,list(str(N)))
    j = len(B)-1
    while not check(B):
        B[j] = 9
        B[j-1] -= 1
        j-=1
    if i== T-1:
        w.write("Case #%s: %s" %(i+1,''.join([str(b) if b != 0 else '' for b in B])))
    else:
        w.write("Case #%s: %s\n" %(i+1,''.join([str(b) if b != 0 else '' for b in B])))
w.close()
print "Done"
