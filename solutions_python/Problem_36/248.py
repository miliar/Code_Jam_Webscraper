
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %04d\n'%(i+1,l))

'''
welcome to code jam
'''
dLeast={
    'w':1,
    'e':3,
    'l':1,
    'c':2,
    'o':3,
    'm':2,
    ' ':2,
    't':1,
    'd':1,
    'j':1,
    'a':1
}

def getCount(str):
    d={
        'w':[],
        'e':[],#3
        'l':[],
        'c':[],#2
        'o':[],#3
        'm':[],#2
        ' ':[],#2
        't':[],
        'd':[],
        'j':[],
        'a':[]
    }
    #print d
    keys = d.keys()
    for i,c in enumerate(str):
        if c in keys:
            d[c].append(i)
    #print d
    if isEmpty(d):
        return 0
    
    removeBeforeW(d)
    #print d
    if isEmpty(d):
        return 0
    
    removeAfterM(d)
    #print d
    if isEmpty(d):
        return 0
        
    count = 0
    
    for o2 in d['o'][1:-1]:
        'welcome t'
        countWelcome_t = 0        
        for o1 in d['o']:
            if o1>o2:
                continue            
            'welc'
            countWelc = 0
            for e1 in d['e']:
                if e1>o1:
                    continue
                countW = len([x for x in d['w'] if x<e1])
                countLC = 0
                for l in d['l']:
                    if l>e1 and  l<o1:
                        for c in d['c']:
                            if c>l and c<o1:
                                countLC += 1
                countWelc += countW*countLC
                if countWelc>10000:
                    countWelc = countWelc%10000
                
            'me t'
            countMe_t = 0
            for _1 in d[' ']:
                if _1<o1 or _1>o2:
                    continue
                countMe = 0
                for m1 in d['m']:
                    if m1>o1 and m1<_1:
                        for e2 in d['e']:
                            if e2>m1 and e2<_1:
                                countMe += 1
                countT = len([x for x in d['t'] if x>_1 and x<o2])
                countMe_t += countMe*countT
                if countMe_t>10000:
                    countMe_t = countMe_t%10000
                
            countWelcome_t += countWelc*countMe_t
            if countWelcome_t>10000:
                countWelcome_t = countWelcome_t%10000
            
        ' code jam'
        count_code_jam = 0
        for e3 in d['e']:
            if e3<o2:
                continue            
            ' cod'
            count_cod = 0
            for o3 in d['o']:
                if o3<o2 or o3>e3:
                    continue
                count_c = 0
                for _2 in d[' ']:
                    if _2<o2 or _2>e3:
                        continue
                    for c2 in d['c']:
                        if c2>_2 and c2<o3:
                            count_c += 1
                countD = len([x for x in d['d'] if x>o3 and x<e3])
                count_cod += count_c*countD
                if count_cod>10000:
                    count_cod = count_cod%10000
            ' jam'
            count_jam = 0
            for a in d['a']:
                if a<e3:
                    continue
                count_j = 0
                for _3 in d[' ']:
                    if _3<e3 or _3>a:
                        continue
                    for j in d['j']:
                        if j>_3 and j<a:
                            count_j += 1
                countM = len([x for x in d['m'] if x>a])
                count_jam += count_j*countM
                if count_jam>10000:
                    count_jam = count_jam%10000
            count_code_jam += count_cod*count_jam
            if count_code_jam>10000:
                count_code_jam = count_code_jam%10000
        count += countWelcome_t*count_code_jam
        if count>10000:
            count = count%10000
    
    return count
        
def isEmpty(d):
    for k,v in d.iteritems():
        if v == [] or len(v)<dLeast[k]:
            return True
    return False

def removeBeforeW(d):
    start = d['w'][0]
    for k,v in d.iteritems():
        if k!='w':
            #print k,v
            v = [x for x in v if x>start]
            #print k,v
            d[k]=v

def removeAfterM(d):
    end = d['m'][-1]
    for k,v in d.iteritems():
        if k!='m':
            #print k,v
            v = [x for x in v if x<end]
            #print k,v
            d[k]=v

f = open('Small.in')
contents = f.readlines()
s =contents[0].split()
n = int(s[0])
print n
lsResult = []
for i in range(1,n+1):
    #print contents[i]     
    lsResult.append( getCount(contents[i]) )
    

#print lsResult
    
wf('x.out',lsResult)
print 'end'