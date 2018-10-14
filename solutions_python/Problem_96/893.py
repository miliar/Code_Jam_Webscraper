f = open('google_02_input','r')
nr = int(f.readline())

def generate(p):
    a = float(p)/3
    b = int(a)
    if b == a:
        return filter(lambda x: max(x)<=10 and min(x)>=0,[[b,b,b],[b-1,b,b+1]])
    elif float(p)%3==2:
        return filter(lambda x: max(x)<=10 and min(x)>=0,[[b,b,b+2],[b,b+1,b+1]])
    elif float(p)%3==1:
        return filter(lambda x: max(x)<=10 and min(x)>=0,[[b,b,b+1],[b-1,b+1,b]])

for a in xrange(0,nr):
    print 'Case #'+str(a+1)+': ',
    line = map(lambda x: int(x), f.readline().split(' '))
    T = line[0] # nr of googlers
    S = line[1] # nr of surprising
    p = line[2] # min value
    t = line[3:]
    val = 0
    surprising = 0
    for a in t:
        # find all single solutions
        scores = generate(a)
        if len(scores)==1:
            if max(scores[0])>=p:
                val += 1
            if max(scores[0])-min(scores[0])==2:
                surprising += 1
        else:
            if max(scores[0])-min(scores[0])<2 and max(scores[0])>=p:
                val += 1
                if max(scores[0])-min(scores[0])==2:
                    surprising += 1
            elif max(scores[1])-min(scores[1])<2 and max(scores[1])>=p:
                val += 1
                if max(scores[1])-min(scores[1])==2:
                    surprising += 1
            elif surprising<S and max(scores[0])>=p:
                surprising += 1
                val += 1
            elif surprising<S and max(scores[1])>=p:
                surprising += 1
                val += 1
            else:
                pass
    print val