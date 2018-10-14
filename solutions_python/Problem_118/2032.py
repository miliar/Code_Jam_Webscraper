def palindrome(nstring):
    if len(nstring)<=1:
        return True
    else:
        if nstring[0]==nstring[-1]:
            return palindrome(nstring[1:-1])
        else:
            return False

def fairandsquareofevenlength(evenlength):
    p2list=[]
    for firsthalf in [str(bin(decimal))[2:] for decimal in range(2**(evenlength/2-1),2**(evenlength/2))]:
        p=firsthalf+firsthalf[::-1]
        p2=int(p)**2
        if palindrome(str(p2)):
            p2list.append(p2)
    p=2*10**(evenlength-1)+2
    p2list.append(p**2)
    return p2list

def fairandsquareofoddlength(oddlength):
    p2list=[]
    for firsthalf in [str(bin(decimal))[2:] for decimal in range(2**((oddlength-1)/2-1),2**((oddlength-1)/2))]:
        for middle in ["0","1","2"]:
            p=firsthalf+middle+firsthalf[::-1]
            p2=int(p)**2
            if palindrome(str(p2)):
                p2list.append(p2)
    p=2*10**(oddlength-1)+2
    p2list.append(p**2)
    p=2*10**(oddlength-1)+10**((oddlength-1)/2)+2
    p2list.append(p**2)
    return p2list

def fairandsquareoflength(length):
    if length ==1:
        return [1,4,9]
    if length % 2:
        return fairandsquareofoddlength(length)
    else:
        return fairandsquareofevenlength(length)

fairandsquarelist=[]
for length in range(1,11):
    fairandsquarelist=fairandsquarelist+fairandsquareoflength(length)

f=open('C-large-1.in')
g=open('C-large-1.out','w')

T=int(f.readline())

for t in range(1,T+1):
    A,B=[int(bound) for bound in f.readline().split()]
    i=0
    fs=fairandsquarelist[i]
    while fs<A:
        i=i+1
        fs=fairandsquarelist[i]
    a=i
    while fs<=B:
        i=i+1
        fs=fairandsquarelist[i]
    fairandsquares=i-a        
    #print >>g, "Case #"+str(t)+": "+str(y)
    print >>g, "Case #"+str(t)+": "+str(fairandsquares)

f.close()
g.close()
