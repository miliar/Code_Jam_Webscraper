f = open('google_03_input','r')
nr = int(f.readline())

def generate(A,B):
    l = []
    for b in xrange(int(A),int(B)):
        b = str(b)
        for i in xrange(1,len(b)):
            if int(b[i]) >= int(A[0]) and int(b[i]) <= int(B[0]):
                if int(b) < int(b[i:]+b[0:i]) and int(B) >= int(b[i:]+b[0:i]):
                    if(int(b)<int(b[i:]+b[0:i])): l.append((int(b),int(b[i:]+b[0:i])))
                    else: l.append((int(b[i:]+b[0:i]),int(b)))
    return set(l)

for a in xrange(0,nr):
    A,B = map(lambda x: str(int(x)), f.readline().split(' '))
    print 'Case #'+str(a+1)+': '+str(len(generate(A,B)))