def bathroom(s):
    G = {int(s[0]):1} # here gaps will be stored(gapsize:count)
    K = int(s[1]) #number of people
    #N = int(s[0])
    i=0
    while i<K:
        m = max(k for k, v in G.iteritems())
        c = G.pop(m) # number of gaps of such size
        r = m/2
        l = (m-1)/2 # this integer division should do, l<=r always, and max=r, min=l, ALWAYS MUST
        if i+c>K: # we reached the needed gapsize, l,r
            break
        i+=c
        if G.has_key(r):
            G[r]=G[r]+c
        else:
            G[r]=c
        if G.has_key(l):
            G[l]=G[l]+c
        else:
            G[l]=c
    
    return str(`r` + ' ' + `l`)

f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(f.readline().split(' '))

f.close()
f = open('output.txt', 'w')
for i in range(T):
    #print i
    f.write("Case #%s: %s\n" % (i+1, bathroom(tcs[i])))
f.close()

