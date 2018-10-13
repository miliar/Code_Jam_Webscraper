f = open('Google Bathroom Stalls Small.in','r')
g = open('Google Bathroom Stalls Small.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def pick_stall(a):
    gap = 0
    x = -1
    y = -1
    for i in range(1,len(a)):
        if a[i] - a[i-1] > gap:
            gap = a[i] - a[i-1]
            x = a[i-1]
            y = a[i]
    return (x+y)/2

def brute_force(n,k):
    if n == k:
        return (0,0)
    a = [0,n+1]
    for  i in range(k-1):
        x = pick_stall(a)
        a.append(x)
        a.sort()
    x = pick_stall(a)
    p = len(a) -1
    while a[p] > x:
        p -= 1
    t = (x-a[p]-1,a[p+1]-x-1)
    m = max(t)
    m2 = min(t)
    return m,m2


cases = int(f.readline())
answers = []
for i in range(cases):
    n,k = [int(x) for x in f.readline().rstrip().split(' ')]
    m,m2 = brute_force(n,k)
    answers.append("%s %s" %(str(m),str(m2)))
Google_print(g,answers)
f.close()
g.close()
    
    



    


            
        
    