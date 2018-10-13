t = int(raw_input())  # read a line with a single integer
p=[]
z=0
r=0

for b in xrange(1, t + 1):
    n,m=raw_input().split()
    d=list(n)
    z=0
    i=0
    if d[-1] == '-':
        z+=1
        for k in range(-int(m), 0):
            if d[k] == '-':
                d[k] = '+'
            else:
                d[k] = '-'
    while i<=len(n)-int(m):
        if d[i]=='-':
            z += 1
            for k in range (0,int(m)):
                if d[i+k]=='-':
                    d[i+k]='+'
                else:
                    d[i+k]='-'
        i+=1


    if d.count('+')==len(n):
        p.append('Case #' + str(b) + ': ' + str(z))
    else:
        p.append('Case #' + str(b) + ': ' + 'IMPOSSIBLE')
for g in p:
    print g

