import re

input = file("A-small-attempt1.in","r").readlines()
l,d,n = input[0].split();

def str2list(s):
    d = []
    s = s.strip()
    if s.find('(') >= 0:
        while s.find('(') >= 0:
            f,e = s.find('('),s.find(')')
            d.extend(list(s[0:f]))
            d.append(list(s[f+1:e]))
            s = s[e+1:len(s)]
        d.extend(list(s))
        return d
    else:
        return list(s)
            
        
    

#s = "asddada(asdada)sadas(asdasd)(asdasda)"
#p = "saddasdasdadasd"
#q = "(asdasdas)asdasda(asdadasda)"
#print s,'\n',str2list(s)
#print p,'\n',str2list(p)
#print q,'\n',str2list(q)

def check(x,y):
    for q in range(0,len(x)):
        #print q,len(y)
        if x[q] not in y[q]:
            return 0
    return 1    


j = 1
m = {}
while j < int(n)+1:
    m[j] = 0
    for i in range(1,int(d)):
        #print input[int(d)+j],str2list(input[int(d)+j])
        if check(list(input[i].strip()),str2list(input[int(d)+j])):
            #print input[i],str2list(input[int(d)+j])
            m[j] += 1
        else:
            continue
    print j,m[j]
    j+=1

t = file("output","w")
for k in m:
    t.write("Case #%s:%s \n"%(k,m[k]))
t.close()

