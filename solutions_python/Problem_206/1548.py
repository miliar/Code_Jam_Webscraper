f = open('Google Steed 2 Large.in','r')
g = open('Google Steed 2 Large.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def catch_up(pos1,v1,pos2,v2):
    if pos1 < pos2 and v1 <= v2:
        return (float('inf'),float('inf'))
    d = pos2 - pos1
    v = v1-v2
    t = float(d)/v
    p = pos1 + v1*t
    return t,p

def logjam(a,dest):
    a.sort()
    bn = dest
    pos2,v2 = a.pop()
    tt = float(dest-pos2)/v2
    while a:
        pos1,v1 = a.pop()
        t,p = catch_up(pos1,v1,pos2,v2)
        if t == float('inf'):
            tt = float(dest-pos1)/v1
        pos2,v2 = pos1,v1
    return float(dest)/tt

def maxspeed(a,dest):
    a.sort()
    pos1,v1 = a[0]
    t = float(dest-pos1)/v1
    speed = float(dest)/t
    for horse in range(1,len(a)):
        p,v = a[horse]
        tcheck = float(dest-p)/v
        if tcheck > t:
            t = tcheck
            speed = float(dest)/t
    return speed

def logjam2(a,dest):
    slowest = float('inf')
    pos = None
    for p,v in a:
        if v < slowest:
            slowest = v
            pos = p
    t = float(dest-pos)/slowest
    return dest/t
            

cases = int(f.readline())
answers = []
for i in range(cases):
    dest,horses = [int(x) for x in f.readline().rstrip().split(' ')]
    a = []
    for j in range(horses):
        p,v = [int(x) for x in f.readline().rstrip().split(' ')]
        a.append((p,v))
    answers.append(maxspeed(a,dest))
Google_print(g,answers)

f.close()
g.close()
        
    